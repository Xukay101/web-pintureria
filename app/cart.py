from flask import Blueprint, render_template, request, redirect, url_for, flash, session

bp = Blueprint('cart', __name__)

@bp.route('/cart')
def show_cart():
    
    producto1 = {"nombre":"Latex","descripcion":"Pintura interior","img_perfil":"images/azul_glaciar.jpg","precio":100.5,"cantidad":4}
    producto2 = {"nombre":"Esmalte","descripcion":"Pintura interior","img_perfil":"images/azul_glaciar.jpg","precio":112.5,"cantidad":7}
    cart = [producto1,producto2]
    total = sum([product["precio"] for product in cart])
    contador_items = len(cart)
    
    return render_template('cart.html',cart = cart,total = total,contador_items = contador_items)

@bp.route('/delete_to_cart')
def delete_to_cart():
    pass

@bp.route('/add_to_cart')
def add_to_cart():
    pass

@bp.route('/get_date_to_buy')
def get_date_to_buy():
    pass

@bp.route('/send_order')
def send_order():
    pass
