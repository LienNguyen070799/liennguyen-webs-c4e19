from flask import Flask, render_template
# from mongoengine import *
import mlab
from models.service import Service
from customer import Customer
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')
# design database
@app.route('/search/<g>')
def search(g) :
    all_service = Service.objects(gender = g, yob__lte = 1998, address__contains = "Hanoi")
    return render_template('search.html', all_service = all_service)

@app.route('/customer')
def customer() :
    all_customer = Customer.objects()
    return render_template('customers.html', all_customer = all_customer)
@app.route('/not_yet_connected_customer')
def not_customer() :
    not_customer = Customer.objects(connected = False, gender = 1)
    if len(not_customer) <= 10 :
        new_customer = not_customer
    else:
        new_customer = not_customer[0:10]
    return render_template('not_customer.html', not_customer = new_customer)

if __name__ == '__main__':
  app.run(debug=True)
 