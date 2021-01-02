
# adapted from: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras import backend
from tensorflow.keras.models import load_model

app = Flask(__name__)

  


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#


@app.route('/predict', methods=['POST'])
def predict():
    # data = [request.form['speed']]
    data = float(request.get_json()["speed"])
    model = tf.keras.models.load_model("model.h5")
    

    predict = model.predict([data])
   # print(predictPower = model.predict(data))
    #print(predictor)
    #print(data)

    #data = datatype (float)
    preds = predict.tolist()
    print(predict)
    return {'predict': preds[0]}

    #predictions = app.predictor.predict(data)
    # print('INFO Predictions: {}'.format(predictions))

    # class_ = np.where(predictions == np.amax(predictions, axis=1))[1][0]

    # return render_template('index.html', pred=class_)


def main():
    """Run the app."""
    app.run(port=5001, debug=True)  # nosec


if __name__ == '__main__':
    main()

