import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Simulate dataset
np.random.seed(42)
n_samples = 100

df = pd.DataFrame({
    'temperature': np.random.normal(40, 5, n_samples),
    'current_density': np.random.normal(5, 1.5, n_samples),
    'cycle_count': np.random.randint(100, 1000, n_samples),
    'electrolyte_pH': np.random.normal(7, 0.5, n_samples),
    'voltage': np.random.normal(3.7, 0.2, n_samples),
})

# Target variable: corrosion_rate
df['corrosion_rate'] = (
    0.1 * df['temperature'] +
    0.3 * df['current_density'] +
    0.002 * df['cycle_count'] -
    0.5 * df['electrolyte_pH'] +
    0.8 * df['voltage'] +
    np.random.normal(0, 1, n_samples)
)

# Split features and target
X = df.drop(columns='corrosion_rate')
y = df['corrosion_rate']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump(model, "corrosion_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model and scaler saved!")
