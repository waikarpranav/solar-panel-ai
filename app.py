import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- Page Config ---
st.set_page_config(
    page_title="SolarPanelAI - Solar Forecasting",
    page_icon="☀️",
    layout="centered"
)

# --- Style ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Load Model & Scaler ---
@st.cache_resource
def load_assets():
    # Use absolute paths relative to this script
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, 'model/solar_model.pkl')
    scaler_path = os.path.join(base_path, 'model/scaler.pkl')
    
    if os.path.exists(model_path) and os.path.exists(scaler_path):
        try:
            model = joblib.load(model_path)
            scaler = joblib.load(scaler_path)
            return model, scaler
        except Exception as e:
            st.error(f"Error loading model files: {e}")
            return None, None
    return None, None

model, scaler = load_assets()

# --- Header ---
st.title("☀️ SolarPanelAI")
st.markdown("### AI-Based Solar Energy Forecasting & Diagnostics")
st.write("Provide the weather parameters below to predict the solar energy generation (kWh).")

st.divider()

# --- Input Section ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🕒 Time & Solar")
    hour = st.slider("Hour of Day", 0, 23, 12)
    irradiance = st.number_input("Irradiance (W/m²)", min_value=0.0, max_value=1200.0, value=500.0)

with col2:
    st.subheader("🌤️ Weather")
    temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0)
    cloud = st.slider("Cloud Cover (%)", 0, 100, 20)

month = st.selectbox("Select Month", options=range(1, 13), format_func=lambda x: [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
][x-1])

st.divider()

# --- Prediction Logic ---
if st.button("⚡ Generate Prediction"):
    if model and scaler:
        # Features: [hour, irradiance_W_m2, temperature_C, cloud_cover_percent, month]
        feature_cols = ['hour', 'irradiance_W_m2', 'temperature_C', 'cloud_cover_percent', 'month']
        input_data = pd.DataFrame([[hour, irradiance, temp, cloud, month]], columns=feature_cols)
        
        # Scale input
        input_scaled = scaler.transform(input_data)
        
        # Predict
        prediction = model.predict(input_scaled)[0]
        
        # Display Result
        st.success(f"### Predicted Energy: **{prediction:.2f} kWh**")
        
        # Diagnostics
        if prediction > 3.5:
            st.info("💡 **Diagnostic**: Peak production period detected. Optimal for high-demand tasks.")
        elif prediction < 1.0:
            st.warning("☁️ **Diagnostic**: Low energy yield. Check for heavy cloud cover or low irradiance.")
        else:
            st.info("☀️ **Diagnostic**: Moderate energy generation. Normal operational conditions.")
    else:
        st.error("Error: Model files not found in `model/` directory. Please run the training notebooks first.")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built with ❤️ for Energy Sustainability</p>", unsafe_allow_html=True)
