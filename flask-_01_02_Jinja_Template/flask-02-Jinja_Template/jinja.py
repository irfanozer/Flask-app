from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=50, number2=20)

@app.route("/<string:num1>/<string:num2>")
def number(num1, num2):
    return render_template("index.html", number1=int(num1), number2=int(num2))

@app.route("/multiply/<string:num1>/<string:num2>")
def multiply(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return render_template("body.html", value1=int(num1), value2=int(num2), sum=int(num1)*int(num2))
    else:
        return "Please enter valid number"


if __name__== "__main__":
    app.run(debug=True, port=3000)
    # app.run(host= '0.0.0.0', port=8081)