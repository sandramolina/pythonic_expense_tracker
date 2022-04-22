from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_bp = Blueprint("merchants", __name__)

@merchants_bp.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/merchants.html', merchants = merchants)

@merchants_bp.route('/merchants/new')
def new_human():
    return render_template("merchants/new.html")

@merchants_bp.route('/merchants', methods=['POST'])
def create_merchant():
    name = request.form['name']
    new_merchant = Merchant(name)
    merchant_repository.save(new_merchant)
    return redirect('/merchants')

@merchants_bp.route('/merchants/<id>/delete', methods = ['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')

@merchants_bp.route('/merchants/<id>/edit')
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('/merchants/edit.html', merchant = merchant, name = merchant.get_merchant_name())

@merchants_bp.route('/merchants/<id>', methods = ['POST'])
def update_merchant(id):
    name = request.form['name']
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')