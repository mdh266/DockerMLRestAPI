from flask import Flask, request, jsonify

import joblib
import pandas as pd
import xgboost as xgb

app = Flask(__name__)


@app.route("/")
def hello():
  return "Hello World!"

@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':
    try:
      json = request.json

      df   = pd.DataFrame(columns=json['columns'],
                          data=json['data'])

      model = joblib.load("model/xgbmodel.joblib")

      result = model.predict(xgb.DMatrix(df))
      
      return jsonify(str(list(result)))

    except:
      return jsonify({'trace': traceback.format_exc()})


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)