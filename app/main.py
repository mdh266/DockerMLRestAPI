from flask import Flask, request
import json

import joblib
import pandas as pd
import xgboost as xgb


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':
    try:
      data = request.json

      df   = pd.DataFrame(columns=data['columns'],
                          data=data['data'])

      model = joblib.load("model/xgbmodel.joblib")

      result = model.predict(xgb.DMatrix(df))
      
      return json.dumps([float(res) for res in result])

    except:
      return json.dumps({'trace': traceback.format_exc()})


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)