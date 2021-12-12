from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route("/math/<operation>")
def calculate(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    cal = operations[operation](a, b)

    return str(cal)


@app.route("/add")
def add_data():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    sum = add(a, b)
    return str(sum)


@app.route("/sub")
def sub_data():
    a_data = int(request.args.get("a"))
    b_data = int(request.args.get("b"))

    diff = sub(a_data, b_data)
    return str(diff)


@app.route("/mult")
def mult_data():
    a_data = int(request.args.get("a"))
    b_data = int(request.args.get("b"))

    prod = mult(a_data, b_data)
    return str(prod)


@app.route("/div")
def div_data():
    a_data = int(request.args.get("a"))
    b_data = int(request.args.get("b"))

    quo = div(a_data, b_data)
    return str(quo)
