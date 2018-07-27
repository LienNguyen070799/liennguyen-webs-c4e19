from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"

@app.route('/user/<username>')
def user_profile(username) :
    users = {'Tuấn Anh':{'name' : 'Huỳnh Tuấn Anh', 'age' : 23, 'gender' : 'male'},
        'Anh Quân':{'name ' : 'Nguyễn Anh Quân', 'age' : 22, 'gender' : 'male'},
        'Ngọc Anh':{'name' : 'Nguyễn Ngọc Anh', 'age' : 23,'gender' : 'female'},
        'Liên':{'name' : 'Nguyễn Thị Liên', 'age' : 19,'gender' : 'female'}}
    return render_template('ex02.html',users = users,username = username)
if __name__ == '__main__':
  app.run(debug=True)
 