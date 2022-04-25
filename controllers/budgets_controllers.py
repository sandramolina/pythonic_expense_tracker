from flask import Blueprint, Flask, redirect, render_template, request

budgets_bp = Blueprint("budgets", __name__)

@budgets_bp.route('/budget_mgmt')
def budget_mgmt():
    return render_template('budgets/budget_mgmt.html')