from flask import Flask, request, render_template # type: ignore
from flask_mail import Mail, Message # type: ignore

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'bagavathithangavelias@gmail.com'
app.config['MAIL_PASSWORD'] = 'slzonreuyyqcxphf'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message']
        
        msg = Message("New Contact Form Submission", sender=email, recipients=[email])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message_body}"
        mail.send(msg)
        
        return "Message Sent!"
    
    return render_template('mail.html')
     

if __name__ == '__main__':
    app.run(debug=True)
