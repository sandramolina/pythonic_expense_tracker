from unicodedata import category
from db.run_sql import run_sql
from models.category import Category

def save(category):
    sql = "INSERT INTO categories (name) VALUES (%s) RETURNING id"
    values = [category.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id

def select_all():
    categories = []
    sql = "SELECT * FROM categories"
    results = run_sql(sql)
    for result in results:
        category = Category(result["name"], result["id"])
        categories.append(category)
    return categories
