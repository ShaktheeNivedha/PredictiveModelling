from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load trained models
energy_model = joblib.load("C:/Users/Muthukumar/Desktop/deployment/project/Energy_consumption/rf_model_full.pkl")  # Energy consumption model
water_model = joblib.load("C:/Users/Muthukumar/Desktop/deployment/project/Water_consumption/rf_model_full.pkl")  # Water consumption model

@app.route('/predict/energy', methods=['POST'])
def predict_energy():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extract features
        features = [
            data.get("day_of_week"), data.get("month"), data.get("hour"),
            data.get("weekend"), data.get("holiday"), data.get("temperature"),
            data.get("humidity"), data.get("wind_speed"), data.get("solar_radiation"),
            data.get("building_size"), data.get("occupants"), data.get("building_type"),
            data.get("hvac_usage"), data.get("lighting_usage"), data.get("appliance_load"),
            data.get("prev_hour"), data.get("prev_day"), data.get("prev_week")
        ]

        # Validate features
        if None in features:
            return jsonify({"error": "Missing or invalid features"}), 400

        # Make prediction
        prediction = energy_model.predict([features])[0]
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict/water', methods=['POST'])
def predict_water():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extract features
        features = [
            data.get("day_of_week"), data.get("month"), data.get("temperature"),
            data.get("rainfall"), data.get("holiday"), data.get("prev_day_water"),
            data.get("building_size"), data.get("household_members")
        ]

        # Validate features
        if None in features:
            return jsonify({"error": "Missing or invalid features"}), 400

        # Make prediction
        prediction = water_model.predict([features])[0]
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)