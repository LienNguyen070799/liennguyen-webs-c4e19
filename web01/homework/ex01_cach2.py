from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Trang chủ không có gì cả'


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height) :
    bmi = (weight*10**4)/(height**2)
    return render_template("bmi.html", bmi = bmi)
if __name__ == '__main__':
  app.run(debug=True)
 