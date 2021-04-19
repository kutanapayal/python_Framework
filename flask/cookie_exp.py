from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('cookie_Index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
      
      resp = make_response(render_template('readcookie.html'))
      resp.set_cookie('userID', user)
      
      return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
   app.run('ec2-34-202-158-221.compute-1.amazonaws.com',5000,debug = True)