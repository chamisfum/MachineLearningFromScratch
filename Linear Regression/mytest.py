from LinearModel import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

# Read csv data
df = pd.read_csv('https://github.com/hattafudholi/dataset/raw/master/data.csv', header=None)

# Split data
data_train = df[:20]
X_train = data_train[0].values.reshape(-1, 1)
y_train = data_train[1].values.reshape(-1, 1)

data_test = df[20:]
X_test = data_test[0].values.reshape(-1, 1)
y_test = data_test[1].values.reshape(-1, 1)

# Initialize model
model = LinearRegression()

# Fit model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Evaluate model
model.evaluate(y_test, y_pred, 'all')

# Plot the reslut
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.show()