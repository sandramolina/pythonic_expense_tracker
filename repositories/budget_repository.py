from db.run_sql import run_sql
from models.budget import Budget

import repositories.expense_repository as expense_repository

def save(budget):
    sql = "INSERT INTO budgets (total_budget, periodicity) VALUES (%s, %s) RETURNING id"
    
    values = [budget.get_total_budget(), budget.get_budget_periodicity()]
    results = run_sql(sql, values)
    id = results[0]['id']
    budget.id = id

def select_all():
    budgets = []
    
    sql = "SELECT * FROM budgets"
    results = run_sql(sql)

    for result in results:
        budget = Budget(result["total_budget"], result["periodicity"], result["id"])
        budgets.append(budget)
    return budgets

def select(id):
    budget = None

    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        budget = Budget(result["total_budget"], result["periodicity"], result["id"])
    return budget

def delete(id):
    sql = "DELETE FROM budgets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(budget):
    sql = "UPDATE budgets SET (total_budget, periodicity) = (%s, %s) WHERE id = %s"
    values = [budget.total_budget, budget.periodicity, budget.id]
    run_sql(sql, values)

def alert():
    sql = "SELECT * FROM budgets"
    all_budgets = run_sql(sql)

    total_budget = 0
    for budget in all_budgets:
        total_budget += int(budget['total_budget'])
    
    balance = 0
    total_expenses = expense_repository.get_total_expenses()
    
    balance = total_budget - total_expenses

    if balance > 10:
        return f'Your budget balance is {balance}'
    elif balance < 10 and balance > 0:
        return f'Your budget balance is {balance} and you are running out of money'
    elif balance == 0:
        return f'Your budget balance is {balance}, you have run out of money'
    else:
        return f'Your budget balance is {balance}, you are overspending'