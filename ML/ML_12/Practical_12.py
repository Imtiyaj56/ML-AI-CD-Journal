import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import tensorflow as tf

# ---------------- NumPy ----------------
data = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(data)
print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))


# ---------------- Pandas ----------------
df = pd.DataFrame({
    'Age': [20, 21, 22, 23, 24],
    'Marks': [65, 70, 75, 80, 85]
})

print("\nPandas DataFrame:")
print(df)

print("\nMean Marks:", df['Marks'].mean())


# ---------------- Scikit-learn ----------------
X = np.array([[10], [20], [30], [40], [50]])
y = np.array([15, 25, 35, 45, 55])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nScaled Data using Scikit-learn:")
print(X_scaled)

model = LinearRegression()
model.fit(X, y)

print("\nPredicted value for X = 60:")
print(model.predict([[60]])[0])


# ---------------- TensorFlow ----------------
tensor = tf.constant([[1, 2], [3, 4]])

print("\nTensorFlow Tensor:")
print(tensor)

print("\nTensor Addition:")
print(tensor + 2)