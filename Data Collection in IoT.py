import numpy as np
import pandas as pd


def generate_synthetic_data(num_samples=1000):
    # Simulate normal sensor data
    normal_data = np.random.normal(loc=0.0, scale=1.0, size=(num_samples, 3))
    
    # Introduce anomalies
    anomaly_data = np.random.normal(loc=5.0, scale=1.0, size=(int(num_samples * 0.1), 3))
    
    data = np.vstack([normal_data, anomaly_data])
    np.random.shuffle(data)
    
    return data

data = generate_synthetic_data()
df = pd.DataFrame(data, columns=['sensor1', 'sensor2', 'sensor3'])
print(df.head())
