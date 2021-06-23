from flask import Flask,request
from sklearn.pipeline import Pipeline
import numpy as np
import joblib
import json


app = Flask(__name__)

# inisialize predected volume
predected_data = 0.0

# load pipeline
pipeline = joblib.load('transform_predict.joblib')

print('0')

@app.route("/")
def home():
    return "Hello world"

print('1')

@app.route("/makePrediction", methods=["POST", "GET"])
def makePrediction():
    
    print('2')


    global predected_data
    global pipeline
    
    print('3')


    if request.method == "POST":
        #  get data
        
        print('4')

        test_data = request.get_json()

        # data preparation
        test_data = test_data["volume"][-29:]
        test_data = np.array(test_data).reshape(-1, 1)

        # using pipeline
        transformed_data = pipeline['scaler'].transform(test_data).T
        transformed_data = np.reshape(transformed_data, (transformed_data.shape[0], 1, transformed_data.shape[1]))
        predected_data = pipeline['model'].predict(transformed_data)

        # invert predictions (output)
        predected_data = pipeline['scaler'].inverse_transform(predected_data)[0][0]

        
    print('5')

    pred_obj = {"prediction": float(predected_data)}
    json_dump = json.dumps(pred_obj)

    print('\n', json_dump)

    return json_dump


      
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", threaded=False)
