from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sumar")
def sumar():
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    return f"<p>Suma: {a + b}</p>"
