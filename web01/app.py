from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')   
# trang chu
def index():
    posts = [
    {"title": "tho con coc",
    "content": """Hôm nay trăng cao quá \n
    Anh muốn hôn vào má""",
    "author" : "boss",
    "gender" :1
    },
    {"title" : "tho xam",
    "content" : "Ngoi buon ...",
    "author" : "Lien",
    "gender" :0
    }
    ]
    
    return render_template(
        'index.html',
        posts = posts)
    # server + database = render template

@app.route('/Hello')
# di vao 1 route
def hello() :
    return 'Hello c4e 19'

@app.route('/say-hi/<name>/<age>')
def say_hi(name,age):
    return 'Hi {0}, you are {1} years old'.format(name,age)
if __name__ == '__main__':
  app.run(debug=True)
#  server chay lien tuc,debug = true de cap nhat lien tuc nhung code moi nhat
# request parameter