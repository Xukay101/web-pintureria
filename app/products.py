from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import json
bp = Blueprint('products', __name__)

@bp.route('/products')
def products():
    return render_template('products.html', products=get_products())
    

def get_products():
    with open("app/products.json", "r") as file:
        content = file.read()
    products = json.loads(content)
    return products
    