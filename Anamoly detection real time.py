# Simulate real-time data processing on edge device
def detect_anomaly(new_data):
    scaled_data = loaded_scaler.transform(new_data)
    predictions = loaded_model.predict(scaled_data)
    
    # Calculate reconstruction error
    reconstruction_error = np.mean(np.abs(predictions - scaled_data), axis=1)
    anomaly_threshold = 0.5  # This threshold should be determined based on validation data
    
    anomalies = reconstruction_error > anomaly_threshold
    return anomalies, reconstruction_error

# Simulated real-time data
new_data = generate_synthetic_data(num_samples=10)
anomalies, reconstruction_errors = detect_anomaly(new_data)
print("Anomalies Detected:", anomalies)
print("Reconstruction Errors:", reconstruction_errors)
