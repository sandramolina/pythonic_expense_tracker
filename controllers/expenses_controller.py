from flask import Blueprint, Flask, redirect, render_template, request
from models.budget import Budget

from models.expense import Expense

import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository
import repositories.expense_repository as expense_repository
import repositories.budget_repository as budget_repository

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route('/dashboard')
def expenses():
    expenses = expense_repository.select_all()
    merchants = merchant_repository.select_all()
    total_expenses = expense_repository.get_total_expenses()  
    categories = category_repository.select_all()
    return render_template('dashboard.html', expenses = expenses, total_expenses = total_expenses, merchants = merchants, categories = categories, subtotal_expenses_merchant = 0, subtotal_expenses_category = 0, selected_id = None)

@expenses_bp.route('/')
def new_expense():
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()

    balance_alert = budget_repository.alert()

    return render_template('index.html', all_merchants = merchants, all_categories = categories, balance_alert = balance_alert)

@expenses_bp.route('/', methods = ['POST'])
def create_expense():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']

    merchant_id = request.form['merchant_id']
    category_id = request.form['category_id']

    merchant_object = merchant_repository.select(merchant_id)
    category_object = category_repository.select(category_id)

    new_expense = Expense(date, merchant_object, category_object, amount, description)
    expense_repository.save(new_expense)

    return redirect('/dashboard')

@expenses_bp.route('/<id>/edit')
def render_edit_page(id):
    expense = expense_repository.select(id)

    all_merchants = merchant_repository.select_all()
    all_categories = category_repository.select_all()

    return render_template('/edit_transaction.html', expense = expense, merchants = all_merchants, categories = all_categories, selected_id = None)

@expenses_bp.route('/<id>', methods=["POST"])
def update_expense(id):
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']

    merchant_id = request.form['merchant_id']
    category_id = request.form['category_id']

    merchant_object = merchant_repository.select(merchant_id)
    category_object = category_repository.select(category_id)

    expense_to_update = Expense(date, merchant_object, category_object, amount, description, id)
    expense_repository.update(expense_to_update)

    return redirect('/dashboard')

@expenses_bp.route('/<id>/delete', methods = ['POST'])
def delete_expense(id):
    expense_repository.delete(id)
    return redirect('/dashboard')

@expenses_bp.route('/filter_merchant', methods = ['POST'])
def filter_by_merchant():
    if request.form['merchant_id'] == 'select-all':
        subtotal_expenses = expense_repository.get_total_expenses()
        expenses = expense_repository.select_all()
        merchants = merchant_repository.select_all()
        categories = category_repository.select_all()  
        return render_template('dashboard.html', expenses = expenses, merchants = merchants, total_expenses = subtotal_expenses, categories = categories, subtotal_expenses_merchant = subtotal_expenses, selected_id = None)
    
    else:
        id = request.form["merchant_id"]
        selected_id = int(id)
        merchant = merchant_repository.select(id)
        expenses = expense_repository.filter_expenses_merchant(merchant)
        subtotal_expenses = expense_repository.get_subtotal_expenses_by_merchant(merchant)    
        merchants = merchant_repository.select_all()
        categories = category_repository.select_all()   
        return render_template('dashboard.html', expenses = expenses, merchants = merchants, total_expenses = subtotal_expenses, categories = categories, subtotal_expenses_merchant = subtotal_expenses, selected_id = selected_id)

@expenses_bp.route('/filter_category', methods = ['POST'])
def filter_by_category():
    if request.form['category_id'] == 'select-all':
        total_expenses = expense_repository.get_total_expenses()
        expenses = expense_repository.select_all()
        merchants = merchant_repository.select_all()
        categories = category_repository.select_all() 
        return render_template('dashboard.html', expenses = expenses, merchants = merchants, total_expenses = total_expenses, categories = categories, subtotal_expenses_category = total_expenses)
    else:
        id = request.form["category_id"]
        category = category_repository.select(id)
        expenses = expense_repository.filter_expenses_category(category)

        merchants = merchant_repository.select_all()
        categories = category_repository.select_all()
        
        subtotal_expenses = expense_repository.get_subtotal_expenses_by_category(category)

        return render_template('dashboard.html', expenses = expenses, merchants = merchants, total_expenses = subtotal_expenses, categories = categories, subtotal_expenses_category = subtotal_expenses)

@expenses_bp.route('/budget_mgmt', methods = ['POST'])
def add_budget():
    total_budget = request.form['total_budget']
    periodicity = request.form['periodicity']

    budget_object = Budget(total_budget, periodicity)
    budget_repository.save(budget_object)

    return redirect('/')