import os

from dotenv import load_dotenv
from flask import Flask, render_template, flash

def create_app():
    app = Flask(__name__)

    app.secret_key = os.urandom(24)

    load_dotenv()

    app.config.from_mapping(
        SENDGRID_KEY=os.getenv('SENDGRID_KEY'),
        SENDGRID_EMAIL=os.getenv('SENDGRID_EMAIL'),
    )

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/test')
    def test():
        return render_template('base.html')
    
    def page_not_found(error):
        return render_template('not_found.html')

    from . import contact
    app.register_blueprint(contact.bp)
    
    from . import cart
    app.register_blueprint(cart.bp)
    
    app.register_error_handler(404, page_not_found)
    return app