from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("C:\Users\ASUS\Desktop\ML\Crude-Oil-Prediction-Project\server\crude_oil_prediction.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON input
    year = data.get('year')
    month = data.get('month')

    # Validate input
    if year is None or month is None:
        return jsonify({"error": "Please provide year and month"}), 400

    # Prepare input for model (assuming model expects [year, month])
    features = np.array([[year, month]])

    # Predict
    prediction = model.predict(features)

    return jsonify({"predicted_price": float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
