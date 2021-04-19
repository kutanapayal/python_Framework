#---> reference https://www.tutorialspoint.com/flask/flask_mail.htm

from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lasaanishoppings@gmail.com'
app.config['MAIL_PASSWORD'] = 'lasaani@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'lasaanishoppings@gmail.com' 
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', recipients = ['kutanapayal@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "MAil Sent"

if __name__ == '__main__':
   app.run(debug = True)