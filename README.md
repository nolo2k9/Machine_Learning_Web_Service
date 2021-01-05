# Machine Learning Web Service
***
## Keith Nolan: G00351932
***
## Project Goal
***
The goal of this project is to create a web service that uses machine learning to make pre-dictions based on the data set **powerproduction**. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with predicted power values based on speed values sent as **HTTP requests**.

***

## This repository contains
- README.md - Describes the project and how you can set it up.
- train_data_set.ipynb - Contains the model used to predict power values.
- Dockerfile - To run project in a docker container.
- model.h5 - this is the saved model produced.
- requirements.txt - contains the requirements used in this project for docker.
- web-service.py - contains the code used to run this model in the web service.
- templates - contains templates used for the aesthetics of the web application.

***

## How to run this project

- Install **Python** Available at: https://www.python.org/downloads/
- Install **Anaconda** Available at: https://www.anaconda.com/distribution/
- Download this repository from **Github**.
- Move to the project directory

### How to run webservice
```
python web-service.py

```

### How to create Dockerfile
- When in the project directory
- **Run:** docker build -t web-service .

### How to run Dockerfile
- When Docker container has been created run: 
- **Run docker image: **docker run web-service
***
**A bit about Docker:** https://www.docker.com/?utm_source=google&utm_medium=cpc&utm_campaign=dockerhomepage&utm_content=nemea&utm_term=dockerhomepage&utm_budget=growth&gclid=CjwKCAiAudD_BRBXEiwAudakX0q0RQDaFM5vvasyx5Y80I_4oBsdLEM-ZHQ7J-vT7oz4INmMO6ZBehoCEaoQAvD_BwE
***

### Packages used to train model
- tensorflow [Markdown][2]
- tensorflow.keras.models[Markdown][3]
- tensorflow.keras.layers[Markdown][4]
- tensorflow.python.keras[Markdown][5]
- numpy[Markdown][6]
- pandas[Markdown][7]
- sklearn[Markdown][8]
- matplotlib[Markdown][9]


### Packages for web-service
- Flask[Markdown][10]
- tensorflow [Markdown][2]
- numpy [Markdown][6]
- tensorflow.keras [Markdown][3]
- tensorflow.keras.models [Markdown][3]


### References
This is a guide on Markdown [Markdown][1].

[1]: http://en.wikipedia.org/wiki/Markdown 
[2]: https://www.tensorflow.org/
[3]: https://www.tensorflow.org/guide/keras/sequential_model
[4]: https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer
[5]: https://www.tensorflow.org/resources/models-datasets
[6]: https://numpy.org/
[7]: https://pandas.pydata.org/
[8]: https://scikit-learn.org/stable/
[9]: https://matplotlib.org/
[10]: https://flask.palletsprojects.com/en/1.1.x/


