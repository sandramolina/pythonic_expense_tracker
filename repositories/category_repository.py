from db.run_sql import run_sql
from models.category import Category

def save(category):
    sql = "INSERT INTO categories (name) VALUES (%s) RETURNING id"
    values = [category.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id