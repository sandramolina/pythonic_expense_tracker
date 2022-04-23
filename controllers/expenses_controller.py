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





