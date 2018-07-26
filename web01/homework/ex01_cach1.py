from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'

@app.route('/bmi/<int:weight>/<int:height>(in centimeter)')
def bmi(weight,height):
    bmi = (weight*10**4)/(height**2)
    if bmi < 16 :
        return "BMI = " + str(bmi) + " => Severely underweight"
    elif 16 <= bmi < 18.5 :
        return "BMI = " + str(bmi) + " => Underweight"
    elif 18.5 <= bmi < 25 :
        return "BMI = " + str(bmi) + " => Normal"
    elif 25 <= bmi < 30 :
        return  "BMI = " + str(bmi) + " => Overweight"
    else :
        return "BMI = " + str(bmi) + " => Obese"
    
if __name__ == '__main__':
  app.run(debug=True)
 