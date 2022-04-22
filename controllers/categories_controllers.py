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

@categories_bp.route('/categories/<id>/edit')
def edit_category(id):
    category = category_repository.select(id)
    return render_template('/categories/edit.html', category = category, name = category.get_category_name())

@categories_bp.route('/categories/<id>', methods = ['POST'])
def update_category(id):
    name = request.form['name']
    category = Category(name, id)
    category_repository.update(category)
    return redirect('/categories')