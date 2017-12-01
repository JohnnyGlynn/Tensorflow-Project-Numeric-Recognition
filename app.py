#flask imports
import flask as fl
from flask import render_template, request


app = fl.Flask(__name__)

@app.route("/")
def init():
    return render_template('index.html')

@app.route("/uploadfile", methods=['POST'])
def uploadfile():
    
    photo = request.files['photo']

    return photo.filename

if __name__ == "__main__":
    app.run(debug=True)