#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter


@app.route("/count/<int:parameter>")
def count(parameter):
    range_values = range(1, parameter+1)
    # print(range_values)

    string_values = "<br>".join(map(str, range_values))
    # print(string_values)

    return string_values


@app.route("/math/<int:num1><operation><int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return f"<h1>{num1 + num2}</h1>"
    elif operation == "-":
        return f"<h1>{num1 - num2}</h1>"
    elif operation == "*":
        return f"<h1>{num1 * num2}</h1>"
    elif operation == "div":
        return f"<h1>{num1 / num2}</h1>"
    elif operation == "%":
        return f"<h1>{num1 % num2}</h1>"
    else:
        return "<h1>Invalid operation!</h1>"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
