from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>tinh tong</h1>'

@app.route('/sum/<int:x>/<int:y>')
def sum(x,y) :
    return str(x+y)
# return luon ra string

if __name__ == '__main__':
  app.run(debug=True)
 