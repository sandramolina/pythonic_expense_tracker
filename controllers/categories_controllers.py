from flask import Blueprint, Flask, redirect, render_template, request

from models.category import Category
import repositories.category_repository as category_repository

categories_bp = Blueprint("categories", __name__)

@categories_bp.route('/categories')
def categories():
    categories = category_repository.select_all()
    return render_template('categories/categories.html', categories = categories)