from flask import Flask, render_template, flash

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/test')
    def test():
        return render_template('base.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')
 
    return app