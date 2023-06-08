from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash

bp = Blueprint('cart', __name__)

@bp.route('/cart')
def cart():
    return render_template('cart.html')