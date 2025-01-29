from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/welcome')
def welcome():
    return "Welcome to the world of Flask!"

@app.route('/welcome/<name>')
def welcome_name(name):
    return f"Welcome to the world of Flask, {name}!"


if __name__ == '__main__':

    app.run(debug=True, port=5000)
    # app.run(host= '0.0.0.0', port=8081)