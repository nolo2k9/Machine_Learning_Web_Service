
# adapted from: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
# Imports
#Flask
from flask import Flask, request, jsonify, render_template

#Tensorflow
import tensorflow as tf

#Numpy
import numpy as np

#Tensor flow
from tensorflow.keras import backend

from tensorflow.keras.models import load_model

# initialising flask
app = Flask(__name__)

"""
(@/GET)
Get request
route for the index.html file
Will display the main html page
"""
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

"""
(@/POST)
Post request
route for getting the predictions from the model.
Will display predictions when a value is passed in.
"""
@app.route('/predict', methods=['POST'])
def predict():
    #Get the speed value passed in
    data = float(request.get_json()["speed"])
    #Declaring model
    model = tf.keras.models.load_model("model.h5")
    #Predict power based on speed value passed in
    predict = model.predict([data])
    # converting to list
    preds = predict.tolist()
    #Print 
    print(predict)
    #Display results
    return {'predict': preds[0]}


def main():
    """Run the app."""
    app.run(port=5001, debug=True)


if __name__ == '__main__':
    main()
