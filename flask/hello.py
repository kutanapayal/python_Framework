from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'


# /python or /python/ returns the same output However, in case of the first rule (/python),this /python/ URL results in 404 Not Found page
@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()