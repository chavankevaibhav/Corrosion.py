# 🔋 Battery Corrosion Prediction App

This Streamlit app predicts the corrosion rate of aluminum anodes in batteries based on:

- Temperature
- Current Density
- Cycle Count
- Electrolyte pH
- Voltage

## 🚀 How to Use

1. Open the sidebar to input battery parameters.
2. Click "Predict Corrosion Rate".
3. Get an instant prediction of corrosion (μm/year).

## 📦 Dependencies

- streamlit
- scikit-learn
- numpy
- joblib
- pandas

## 🛠 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deploy Online

Push this folder to GitHub and deploy using [Streamlit Cloud](https://streamlit.io/cloud).
