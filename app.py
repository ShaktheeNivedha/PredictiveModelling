import pandas as pd
import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

with open("D:/demo/Energy_consumption/rf_model_full.pkl", "rb") as model_file:
    rf_model_full = pickle.load(model_file)
with open("D:/demo/Energy_consumption/scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

with open("D:/demo/Water_consumption/rf_model_full.pkl", "rb") as water_model_file:
    water_model = pickle.load(water_model_file)
with open("D:/demo/Water_consumption/scaler.pkl", "rb") as water_scaler_file:
    water_scaler = pickle.load(water_scaler_file)

st.set_page_config(layout="wide")
st.title("Consumption Prediction Dashboard")

st.sidebar.markdown("### Select Prediction Model")
model_choice = st.sidebar.selectbox("Select Prediction Model", ["Energy Consumption", "Water Consumption"], index=0, label_visibility="collapsed")

def predict_energy_consumption(input_features):
    input_data = np.array([input_features])
    input_scaled = scaler.transform(input_data)
    prediction = rf_model_full.predict(input_scaled)
    return prediction[0]

def predict_water_consumption(input_features):
    input_data = np.array([input_features])
    input_scaled = water_scaler.transform(input_data)
    prediction = water_model.predict(input_scaled)
    return prediction[0]

if model_choice == "Energy Consumption":
    st.subheader("Energy Consumption Prediction")
    day_of_week = st.number_input("Day of the week", min_value=0, max_value=6, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, step=1)
    hour = st.number_input("Hour", min_value=0, max_value=23, step=1)
    weekend = st.radio("Is it a weekend?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    holiday = st.radio("Is it a holiday?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    temperature = st.number_input("Temperature", step=0.1)
    humidity = st.number_input("Humidity", step=0.1)
    wind_speed = st.number_input("Wind Speed", step=0.1)
    solar_radiation = st.number_input("Solar Radiation", step=0.1)
    building_size = st.number_input("Building Size (sq ft)", min_value=1000, step=10)
    occupants = st.number_input("Number of Occupants", min_value=1, step=1)
    building_type = st.number_input("Building Type", min_value=1, max_value=5, step=1)
    HVAC_usage = st.number_input("HVAC Usage", step=0.1)
    lighting_usage = st.number_input("Lighting Usage", step=0.1)
    appliance_load = st.number_input("Appliance Load", step=0.1)
    previous_hour_consumption = st.number_input("Previous Hour Consumption", step=0.1)
    previous_day_consumption = st.number_input("Previous Day Consumption", step=0.1)
    previous_week_consumption = st.number_input("Previous Week Consumption", step=0.1)
    #electricity_price = st.number_input("Electricity Price", step=0.01)
    
    if st.button("Predict Energy Consumption"):
        input_features = [day_of_week, month, hour, weekend, holiday, temperature, humidity, wind_speed,
                          solar_radiation, building_size, occupants, building_type, HVAC_usage, lighting_usage,
                          appliance_load, previous_hour_consumption, previous_day_consumption, previous_week_consumption,
                          '''electricity_price''']
        prediction = predict_energy_consumption(input_features)
        st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")

elif model_choice == "Water Consumption":
    st.subheader("Water Consumption Prediction")
    day_of_week = st.number_input("Day of the week", min_value=0, max_value=6, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, step=1)
    temperature = st.number_input("Temperature", step=0.1)
    rainfall = st.number_input("Rainfall", step=0.1)
    holiday = st.radio("Is it a holiday?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    lag_1 = st.number_input("Previous Day's Water Consumption", step=0.1)
    building_size = st.number_input("Building Size (sq ft)", min_value=1000.0, step=10.0)
    member_count = st.number_input("Number of Household Members", min_value=1, step=1)
    
    if st.button("Predict Water Consumption"):
        input_features = [day_of_week, month, temperature, rainfall, holiday, lag_1, building_size, member_count]
        prediction = predict_water_consumption(input_features)
        st.success(f"Predicted Water Consumption: {prediction:.2f} Litres")