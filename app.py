#flask imports
import tensorflow as tf

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

@app.route("/whoa")
def whoa():
    # Add ops to save and restore all the variables.
    saver = tf.train.Saver()

    # Later, launch the model, use the saver to restore variables from disk, and
    # do some work with the model.
    with tf.Session() as sess:
    # Restore variables from disk.
        saver.restore(sess, "./mnist92/mnist92.ckpt")
        return("Model restored.")

if __name__ == "__main__":
    app.run(debug=True)