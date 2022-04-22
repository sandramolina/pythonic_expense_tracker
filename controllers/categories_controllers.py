from crypt import methods
from flask import Blueprint, Flask, redirect, render_template, request

from models.category import Category
import repositories.category_repository as category_repository

categories_bp = Blueprint("categories", __name__)

@categories_bp.route('/categories')
def categories():
    categories = category_repository.select_all()
    return render_template('categories/categories.html', categories = categories)

@categories_bp.route('/categories/new')
def new_human():
    return render_template("categories/new.html")

@categories_bp.route('/categories', methods=['POST'])
def create_category():
    name = request.form['name']
    new_category = Category(name)
    category_repository.save(new_category)
    return redirect('/categories')

@categories_bp.route('/categories/<id>/delete', methods = ['POST'])
def delete_category(id):
    category_repository.delete(id)
    return redirect('/categories')