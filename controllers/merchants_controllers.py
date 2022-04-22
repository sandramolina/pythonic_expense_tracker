from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_bp = Blueprint("merchants", __name__)