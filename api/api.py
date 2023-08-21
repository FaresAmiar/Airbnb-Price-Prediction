from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
run_id = "805788121762443315"
model = joblib.load(f"./mlartifacts/{run_id}/495139f333bb49dfae28ad89b5229103/artifacts/model/model.pkl")
dv = joblib.load(f"./mlartifacts/{run_id}/495139f333bb49dfae28ad89b5229103/artifacts/dict_vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.json
    data = request_data['data']

    X = dv.transform(data)

    predictions = model.predict(X)

    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
