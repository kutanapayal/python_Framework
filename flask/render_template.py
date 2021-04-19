from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run('ec2-34-202-158-221.compute-1.amazonaws.com',5000,debug = True)