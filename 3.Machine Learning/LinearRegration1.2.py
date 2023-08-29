# This program predicts a continuous value, such as the price of a house,
# based on a set of features, such as the number of bedrooms and the square footage.
#Linear Regration Method 1

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some data
x = np.linspace(0, 10, 100)
y = 2*x + 5

# Create a linear regression model
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

# Predict the output for a new input
x_new = 12
y_pred = model.predict(x_new.reshape(-1, 1))

# Plot the data and the model
plt.plot(x, y, label="Data")
plt.plot(x_new, y_pred, label="Prediction")
plt.legend()
plt.show()
