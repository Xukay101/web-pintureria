import json

def get_products():
    with open("app/products.json", "r") as file:
        content = file.read()
    products = json.loads(content)
    return products

def get_product(product_id):
    products = get_products()
    for product in products:
        if product['id'] == product_id:
            return product
    return None
