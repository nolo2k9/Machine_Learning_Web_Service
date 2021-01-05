
# adapted from: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras import backend
from tensorflow.keras.models import load_model

# initialising flask
app = Flask(__name__)

"""
Get request
route for the index.html file
Will display the main html page
"""
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    data = float(request.get_json()["speed"])
    model = tf.keras.models.load_model("model.h5")

    predict = model.predict([data])
   
    preds = predict.tolist()
    print(predict)
    return {'predict': preds[0]}


def main():
    """Run the app."""
    app.run(port=5001, debug=True)


if __name__ == '__main__':
    main()
