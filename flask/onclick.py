from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run('ec2-34-202-158-221.compute-1.amazonaws.com',5000,debug = True)