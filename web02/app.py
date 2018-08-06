from flask import *
# from mongoengine import *
import mlab
from models.service import Service
from customer import Customer
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')
# design dat(abase

@app.route('/search/<g>')
def search(g) :
    all_service = Service.objects(gender = g, yob__lte = 1998)
    return render_template('search.html', all_service = all_service)

@app.route('/search/detail/<id>')
def detail(id):
    all_service = Service.objects()
    return render_template('detail.html',all_service = all_service)

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

@app.route("/admin")
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service)

@app.route("/delete/<service_id>/")
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return  "Service not found"

    # return "Deleted" + service_id
@app.route("/new_service", methods =["GET","POST"])
def create() :
    if request.method == "GET" :
        return render_template('new_service.html')
    elif request.method == "POST" :
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        new_service = Service(
        name = name,
        yob = yob,
        phone = phone,
        gender = gender)
        new_service.save()
        return redirect(url_for('admin'))

@app.route("/update_service/<service_id>", methods =["GET","POST"])
def update_service(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        
        if request.method == "GET" :
            return render_template('update_service.html')
        elif request.method == "POST" :
            form = request.form
            name = form['name']
            yob = form['yob']
            phone = form['phone']
            gender = form['gender']
            new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender)
            new_service.save()
            service.delete()
            return redirect(url_for('admin'))
    else :
        return " Not found"


if __name__ == '__main__':
  app.run(debug=True)
#  lỗi bad request lấy thông tin ở form sai,2 thông tin ko khớp nhau, chú ý chỗ if ...
# update
# set input : gg set default input value
# chọn phần tử (giới tính) : radio button
# về xem lại rederict
