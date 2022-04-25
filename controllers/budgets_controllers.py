from flask import Blueprint, Flask, redirect, render_template, request
from models.budget import Budget
import repositories.budget_repository as budget_repository

budgets_bp = Blueprint("budgets", __name__)

@budgets_bp.route('/budget_mgmt')
def budget_mgmt():
    balance_alert = budget_repository.alert()
    return render_template('budgets/budget_mgmt.html', balance_alert = balance_alert)

@budgets_bp.route('/budget_mgmt', methods = ['POST'])
def create_budget():
    total_budget = request.form['total_budget']
    periodicity = request.form['periodicity']

    budget_object = Budget(total_budget, periodicity)
    budget_repository.save(budget_object)

    return redirect('/budget_mgmt')