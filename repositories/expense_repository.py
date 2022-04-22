from db.run_sql import run_sql

# from models.category import Category
# from models.merchant import Merchant
# from models.expense import Expense

# def save(biting):
#     sql = "INSERT INTO expenses (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
#     values = [biting.human.id, biting.zombie.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     biting.id = id

def save(expense):
    sql = "INSERT INTO expenses (date, merchant_id, category_id, amount, description) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [expense.get_expense_date(), expense.merchant.get_merchant_id(), expense.category.get_category_id(), expense.get_expense_amount(), expense.get_expense_description()]
    results = run_sql(sql, values)
    id = results[0]['id']
    expense.id = id

