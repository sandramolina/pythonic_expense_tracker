from db.run_sql import run_sql
from models.budget import Budget

import repositories.expense_repository as expense_repository

def save(budget):
    sql = "INSERT INTO budgets (total_budget, periodicity, budget_status) VALUES (%s, %s, %s) RETURNING id"
    total_expenses = expense_repository.get_total_expenses()
    values = [budget.get_total_budget(), budget.get_budget_periodicity(), budget.budget_status(total_expenses)]
    results = run_sql(sql, values)
    id = results[0]['id']
    budget.id = id

def select_all():
    budgets = []

    sql = "SELECT * FROM budgets"
    results = run_sql(sql)

    for result in results:
        budget = Budget(result["total_budget"], result["id"])
        budgets.append(budget)
    return budgets

def select(id):
    budget = None

    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        budget = Budget(result["total_budget"], result["id"])
    return budget

def delete(id):
    sql = "DELETE FROM budgets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(budget):
    sql = "UPDATE budgets SET total_budget = %s WHERE id = %s"
    values = [budget.total_budget, budget.id]
    run_sql(sql, values)