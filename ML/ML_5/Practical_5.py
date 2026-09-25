import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given data
X = np.array([70, 80, 90, 100, 110, 120, 130, 140, 150, 160])
Y = np.array([7, 7, 8, 9, 12, 12, 15, 14, 13, 17])

# Reshape X
X = X.reshape(-1, 1)

# Create Linear Regression model
model = LinearRegression()
model.fit(X, Y)

# Model parameters
w0 = model.intercept_
w1 = model.coef_[0]

# Predict Y for X = 210
x_new = np.array([[210]])
y_pred = model.predict(x_new)[0]

print("w0 (Intercept):", w0)
print("w1 (Slope):", w1)
print("Predicted Y for X = 210:", y_pred)

# Plot data and regression line
plt.scatter(X, Y, label="Actual Data")

plt.plot(X, model.predict(X), label="Regression Line")

# Show predicted point
plt.scatter(210, y_pred, marker='x', s=100, label="Prediction (X=210)")

plt.xlabel("Advertisement Spend (X)")
plt.ylabel("Increase in Unit Sales (Y)")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid()

plt.show()