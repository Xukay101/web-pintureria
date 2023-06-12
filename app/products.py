from flask import Blueprint, render_template, request, redirect, url_for, flash, session

bp = Blueprint('products', __name__)

@bp.route('/products')
def products():
    return render_template('products.html')
    
    
