import joblib
import tensorflow as tf

# Save the scaler and model
scaler_filename = "scaler.pkl"
model_filename = "anomaly_detection_model.h5"

joblib.dump(scaler, scaler_filename)
model.save(model_filename)

# Load the scaler and model (simulate loading on edge device)
loaded_scaler = joblib.load(scaler_filename)
loaded_model = tf.keras.models.load_model(model_filename)
