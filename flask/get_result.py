from flask import Flask, render_template
app = Flask(__name__)

@app.route('/getresult/<int:score>')
def hello_name(score):
   return render_template('show_result.html', marks = score)

if __name__ == '__main__':
   app.run('ec2-34-202-158-221.compute-1.amazonaws.com',5000)