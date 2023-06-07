import sendgrid
from sendgrid.helpers.mail import *
from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash

bp = Blueprint('contact', __name__)

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/mail', methods=['POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    if request.method == 'POST':
        send_mail(name, email, subject, message)
        flash('El correo electrónico se envió correctamente.')
        return redirect(url_for('contact.contact'))

    flash('El correo electrónico no pudo ser enviado.')
    return redirect(url_for('contact.contact'))

def send_mail(name, email, subject, message):
    my_email = current_app.config['SENDGRID_EMAIL']
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])

    from_email = Email(my_email)
    to_email = To(my_email, substitutions={
        '-name-': name,
        '-email-': email,
        '-subject-': subject,
        '-message-': message,
    })

    html_content = """
        <p>Nombre: -name-</p>
        <p>Correo: -email-</p>
        <p>Asunto: -subject-</p>
        <p>Mensaje: -message-</p>
    """
    mail = Mail(my_email, to_email, 'Nuevo contacto desde la web', html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())