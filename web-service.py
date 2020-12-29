
# adapted from: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras import backend
from tensorflow.keras.models import load_model

app = Flask(__name__)


@app.before_first_request
def load_model_to_app():
    app.predictor = load_model('model.h5')


@app.route('/')
def index():
    return render_template('index.html', pred=0)


@app.route('/predict', methods=['POST'])
def predict():
    data = [request.form['speed'],
            request.form['power']]

    data = np.array([np.asarray(data, dtype=float)])

    predictions = app.predictor.predict(data)
    print('INFO Predictions: {}'.format(predictions))

    class_ = np.where(predictions == np.amax(predictions, axis=1))[1][0]

    return render_template('index.html', pred=class_)


def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000, debug=False)  # nosec


if __name__ == '__main__':
    main()
