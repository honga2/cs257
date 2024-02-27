from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    my_port = 5109
    app.run(host='0.0.0.0', port = my_port)