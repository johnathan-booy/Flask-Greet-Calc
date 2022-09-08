from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def add_values():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{add(a, b)}"


@app.route('/sub')
def sub_values():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{sub(a, b)}"


@app.route('/mult')
def mult_values():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{mult(a, b)}"


@app.route('/div')
def div_values():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{div(a, b)}"


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
