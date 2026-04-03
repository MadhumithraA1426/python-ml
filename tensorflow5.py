import tensorflow as tf
import numpy as np

# FIX: convert to numpy arrays
X = np.array([1, 2, 3])
y = np.array([2, 4, 6])

model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),   # FIX: proper input layer
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

model.fit(X, y, epochs=10)

print(model.predict(np.array([4]))) ## [[6.9386663]]