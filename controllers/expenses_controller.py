from crypt import methods
from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant import Merchant
from models.category import Category
from models.expense import Expense

import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository
import repositories.expense_repository as expense_repository

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route('/dashboard')
def expenses():
    expenses = expense_repository.select_all()
    return render_template('dashboard.html', expenses = expenses)

@expenses_bp.route('/')
def new_expense():
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    return render_template('index.html', all_merchants = merchants, all_categories = categories)

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





