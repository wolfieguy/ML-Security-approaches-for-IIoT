from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

train_data = scaled_data[:800]
test_data = scaled_data[800:]
