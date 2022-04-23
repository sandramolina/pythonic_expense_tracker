from db.run_sql import run_sql

from models.expense import Expense

import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository

def save(expense):
    sql = "INSERT INTO expenses (date, merchant_id, category_id, amount, description) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [expense.get_expense_date(), expense.merchant.get_merchant_id(), expense.category.get_category_id(), expense.get_expense_amount(), expense.get_expense_description()]
    results = run_sql(sql, values)
    id = results[0]['id']
    expense.id = id

def select_all():
    expenses = []

    sql = "SELECT * FROM expenses"
    results = run_sql(sql)

    for result in results:
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        expense = Expense(result['date'], merchant, category, result['amount'], result['description'], result['id'])
        expenses.append(expense)
    return expenses

def select(id):
    expense = None

    sql = "SELECT * FROM expenses WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0] 
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        expense = Expense(result['date'], merchant, category, result['amount'], result['description'], result['id'])
    return expense

def delete(id):
    sql = "DELETE FROM expenses WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM expenses"
    run_sql(sql)

def update(expense):
    sql = "UPDATE expenses SET (date, merchant_id, category_id, amount, description) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [expense.get_expense_date(), expense.merchant.get_merchant_id(), expense.category.get_category_id(), expense.get_expense_amount(), expense.get_expense_description(), expense.id]
    run_sql(sql, values)

def get_total_expenses():
    sql = "SELECT * FROM expenses"
    all_expenses = run_sql(sql)
    total_expenses = 0

    for expense in all_expenses:
        total_expenses += int(expense['amount'])
    
    return total_expenses

def filter_expenses_merchant(merchant):
    expenses = []

    sql = "SELECT expenses.* FROM expenses INNER JOIN merchants ON expenses.merchant_id = merchants.id WHERE merchant_id = %s"

    values= [merchant.id]
    results = run_sql(sql, values)

    for result in results:
        category_id = result['category_id']
        category = category_repository.select(category_id)
        expense = Expense(result['date'], merchant, category, result['amount'], result['description'], result['id'])
        expenses.append(expense)
    
    return expenses

# SELECT exp.date, exp.description, exp.amount, mer.name as merchant, cat.name as category
# FROM expenses as exp
# INNER JOIN categories as cat
# ON cat.id = exp.category_id
# INNER JOIN merchants as mer
# ON mer.id = exp.merchant_id
# WHERE merchant_id = 2

