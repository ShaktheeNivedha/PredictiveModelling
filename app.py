from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained models
energy_model = joblib.load("C:/Users/Muthukumar/Desktop/deployment/project/Water_consumption/rf_model_full.pkl")  # Energy consumption model
water_model = joblib.load("C:/Users/Muthukumar/Desktop/deployment/project/Energy_consumption/rf_model_full.pkl")  # Water consumption model

@app.route('/predict/energy', methods=['POST'])
def predict_energy():
    try:
        data = request.get_json()
        features = [[
            data["day_of_week"], data["month"], data["hour"], 
            data["weekend"], data["holiday"], data["temperature"], 
            data["humidity"], data["wind_speed"], data["solar_radiation"], 
            data["building_size"], data["occupants"], data["building_type"],
            data["hvac_usage"], data["lighting_usage"], data["appliance_load"],
            data["prev_hour"], data["prev_day"], data["prev_week"]
        ]]

        prediction = energy_model.predict(features)[0]

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/predict/water', methods=['POST'])
def predict_water():
    try:
        data = request.get_json()
        features = [[
            data["day_of_week"], data["month"], data["temperature"], 
            data["rainfall"], data["holiday"], data["prev_day_water"], 
            data["building_size"], data["household_members"]
        ]]

        prediction = water_model.predict(features)[0]

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
