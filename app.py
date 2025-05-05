import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("corrosion_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Battery Corrosion Predictor", layout="centered")

st.title("🔋 Battery Corrosion Predictor")
st.markdown("Estimate aluminum-anode corrosion rate to enable proactive maintenance.")

# Sidebar inputs
st.sidebar.header("Enter Parameters:")
temp = st.sidebar.slider("Temperature (°C)", 20, 80, 40)
current = st.sidebar.slider("Current Density (mA/cm²)", 1.0, 10.0, 5.0)
cycles = st.sidebar.slider("Cycle Count", 100, 1000, 500)
pH = st.sidebar.slider("Electrolyte pH", 4.0, 9.0, 7.0)
voltage = st.sidebar.slider("Voltage (V)", 3.0, 4.5, 3.7)

# Predict button
if st.sidebar.button("Predict Corrosion Rate"):
    input_data = np.array([[temp, current, cycles, pH, voltage]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    st.success(f"Estimated Corrosion Rate: **{prediction:.2f} μm/year**")
