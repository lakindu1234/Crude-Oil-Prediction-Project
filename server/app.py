from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # ✅ allow cross-origin requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "crude_oil_prediction.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')

    if year is None or month is None:
        return jsonify({"error": "Please provide both year and month"}), 400

    features = np.array([[year, month]])
    prediction = model.predict(features)

    return jsonify({"predicted_price": float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
