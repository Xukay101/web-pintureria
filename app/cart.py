from .helpers import get_product
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
bp = Blueprint('cart', __name__)

@bp.route('/cart')
def cart():
    if 'cart' not in session or len(session['cart']) == 0:
        cart = []
    else:
        cart = session['cart']
    total_price = sum([product['price'] for product in cart])
    total_items = len(cart)
    
    return render_template('cart.html',cart = cart, total_price=total_price,total_items=total_items)

@bp.route('/delete_to_cart')
def delete_to_cart():
    product_id = int(request.args.get('product_id'))
    for product in session['cart']:
        if product['id'] == product_id:
            session['cart'].remove(product)
            break

    flash("El producto se ha eliminado del carrito correctamente.")
    return redirect('/cart')

@bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = int(request.form['product_id'])
    cant = int(request.form[f'quantity_{product_id}'])

    # Temp
    print("-----------------------")
    print(f"Producto id {product_id}")
    print(f"cantidad {cant}")
    print("-----------------------")

    # Obtener producto
    product = get_product(product_id)

    # Crear carrito si no existe
    if 'cart' not in session:
        session['cart'] = []
    else:
        session['cart'] = session['cart']

    # Si el producto ya esta en el carrito sumar cantidad
    for product_ in session['cart']:
        if product_['name'] == product['name']:
            product_['cant'] += cant 

            # flash("El producto se ha actualizado correctamente.")
            return redirect('/products')

    # agregar producto al carrito
    product['cant'] = cant
    session['cart'].append(product)

    # flash("El producto se ha agregado al carrito correctamente.")
    return redirect('/products')

@bp.route('/send_order')
def send_order():
    pass


