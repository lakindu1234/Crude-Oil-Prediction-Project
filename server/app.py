from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

class CrudeOilPredictionApp:
    def __init__(self):
        # Initialize Flask app
        self.app = Flask(__name__)
        CORS(self.app)  # Allow cross-origin requests

        # Setup model path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, "crude_oil_prediction.pkl")

        # Load model
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        # Define routes
        self.app.add_url_rule("/predict", view_func=self.predict, methods=["POST"])

    def predict(self):
        data = request.get_json()
        year = data.get("year")
        month = data.get("month")

        if year is None or month is None:
            return jsonify({"error": "Please provide both year and month"}), 400

        try:
            # Prepare features
            features = np.array([[year, month]])
            prediction = self.model.predict(features)

            return jsonify({"predicted_price": float(prediction[0])})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def run(self):
        self.app.run(debug=True)


if __name__ == "__main__":
    app_instance = CrudeOilPredictionApp()
    app_instance.run()
