from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# ✅ Get the absolute path to the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Construct full path to the model file
MODEL_PATH = os.path.join(BASE_DIR, "crude_oil_prediction.pkl")

# ✅ Load the trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON input from request
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')

    # Validate input
    if year is None or month is None:
        return jsonify({"error": "Please provide both year and month"}), 400

    # Prepare input for model (assuming model expects [year, month])
    features = np.array([[year, month]])

    # Predict
    prediction = model.predict(features)

    return jsonify({"predicted_price": float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
