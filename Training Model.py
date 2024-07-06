import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(train_data.shape[1],)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(3, activation='sigmoid')  # Use sigmoid activation for reconstruction
])

model.compile(optimizer='adam', loss='mse')
model.summary()

# Train the model
history = model.fit(train_data, train_data, epochs=50, batch_size=32, validation_split=0.2)
