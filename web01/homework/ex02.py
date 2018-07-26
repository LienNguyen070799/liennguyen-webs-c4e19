from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Trang chủ không có gì cả'

@app.route('/user/<username>')
def user_profile(username) :
    users = {
        'Tuấn Anh' : {'name' : 'Huỳnh Tuấn Anh', 'age' : 23, 'gender' : 'male'},
        'Anh Quân' : {'name ' : 'Nguyễn Anh Quân', 'age' : 22, 'gender' : 'male'},
        'Ngọc Anh' : {'name' : 'Nguyễn Ngọc Anh', 'age' : 23,'gender' : 'female'},
        'Liên' : {'name' : 'Nguyễn Thị Liên', 'age' : 19,'gender' : 'female'}
    }
    if username in users :
        return 'Name : {0}, age : {1} , gender : {2}'.format(users[username]['name'],users[username]['age'],users[username]['gender'])
    else:
        return 'User not found'
    
if __name__ == '__main__':
  app.run(debug=True)
