import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Define height (x) and weight (y) data
x = np.array([151, 174, 138, 186, 128, 136, 179, 163, 152, 131]).reshape(-1, 1)
y = np.array([63, 81, 56, 91, 47, 57, 76, 72, 62, 48])

# Create and fit the linear regression model
model = LinearRegression()
model.fit(y.reshape(-1, 1), x)

# Predict values for regression line
y_pred = model.predict(y.reshape(-1, 1))

# Plot the data points
plt.figure(figsize=(8, 6))
plt.scatter(y, x, color='blue', label='Data points', s=50)
plt.plot(y, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel("Weight in kg")
plt.ylabel("Height in cm")
plt.title("Height & Weight Regression")
plt.legend()
plt.grid()

# Save the plot as PNG
plt.savefig("linearregression.png")
plt.show()
