# SolarPanelAI ☀️⚡
### AI-Based Solar Energy Forecasting & Diagnostics System

SolarPanelAI is a machine learning solution designed to predict hourly solar energy generation based on meteorological data. By utilizing historical records of irradiance, temperature, and cloud cover, the system provides accurate energy yield forecasts essential for grid balancing and battery management.

## 🚀 Project Overview
- **Problem**: Solar energy production is highly variable and depends on weather conditions.
- **Solution**: A Random Forest regression model that predicts energy output (kWh) with high precision.
- **Impact**: Enables solar farm operators to optimize energy storage and distribution.

## 🛠️ Tech Stack
- **Languages**: Python
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Visualizations**: Matplotlib, Seaborn
- **Interface**: Streamlit
- **Serialization**: Joblib

## 📂 Folder Structure
```text
SOLAR PROJECT/
├── app.py              # Streamlit Application (Main UI)
├── DATA/               # Raw dataset (CSV)
│   └── solar_weather_data.csv
├── model/              # Serialized model and scaler (.pkl)
│   ├── solar_model.pkl
│   └── scaler.pkl
├── notebooks/          # Step-by-step experimentation
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

## ⚙️ How to Run Locally

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore Data**:
   Open the notebooks in Jupyter Lab or VS Code to see the ML workflow.

3. **Start the App**:
   ```bash
   streamlit run app.py
   ```

## 📊 Sample API Response
```json
{
  "status": "success",
  "prediction_kWh": 42.5678,
  "units": "kWh"
}
```

## 🔮 Future Improvements
- Integration with live weather APIs (e.g., OpenWeatherMap).
- Support for LSTM models to handle temporal dependencies better.
- Frontend dashboard using React or Streamlit.

---
*Developed with Senior Engineering Standards* 🛠️
