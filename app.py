#flask imports
import flask as fl
from flask import render_template


app = fl.Flask(__name__)

@app.route("/")
def init():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()