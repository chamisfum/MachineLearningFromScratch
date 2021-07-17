# Machine Learning From Scratch
**Created by** : [moch. chamdani mustaqim](https://github.com/chamisfum)<br><br>
This is my machine learning module developed from scratch without any import library.

This repo are include some of ML model like:
* Simple Linear Regression


### User guide:
-----------------------------------------------

#### Import the package
```py
from LinearModel import LinearRegression
```

#### Define a model
```py
model = LinearRegression()
```

#### Train the model
```py
print(model.fit(X_train, y_train))
```

You will get the list of intercept and slope value (look like this).
```py
[-1.5745162975881755, 1.4212209690495088]
```

#### Create a prediction
```py
y_pred = model.predict(X_test)
```

#### Evaluate the model
```py
model.evaluate( actual = y_test, predicted = y_pred, matric = 'all')
```

In this module was already define some evaluation matric like bellow. You can use one of the evaluation matric mode to evaluate your model.
```
'mae' : Get MAE (mean absolute error) evaluation value of the model.
'mse' : Get MSE (mean square error) evaluation value of the model.
'rmse': Get RMSE (root mean square error) evaluation value of the model.
'r2'  : Get R^2 error evaluation of the model.
'all' : Get the evaluation value of all matrices either ('mae', 'mse', 'rmse' or 'r2').
```
