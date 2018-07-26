from flask import Flask,redirect
app = Flask(__name__)


@app.route('/')
def index():
    return 'Information about me'

@app.route('/about-me/')
def about_me () :
    intro = """Hello,I'm Liên.
    I'm 19 years old and i am a student at Ha Noi university of science and technology.
    I like eating very much.^^
    Hết rồi.:3
    """
    return intro

@app.route('/school')
def school () :
    return redirect ('http://techkids.vn ')
    
if __name__ == '__main__':
  app.run(debug=True)
 