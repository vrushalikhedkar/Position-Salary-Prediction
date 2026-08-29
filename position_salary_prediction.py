# Position Salary Prediction
# Machine Learning Project
# Converted from Jupyter Notebook

# ------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

# ------------------------------------------------------------
dataset = pd.read_csv('Position_Salaries.csv')

# ------------------------------------------------------------
dataset

# ------------------------------------------------------------
dataset.describe()

# ------------------------------------------------------------
X = dataset[["Level"]]
y = dataset["Salary"]

# ------------------------------------------------------------
X

# ------------------------------------------------------------
y

# ------------------------------------------------------------
plt.scatter(X, y)
plt.title("Position Level vs Salary")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# ------------------------------------------------------------
from sklearn.linear_model import LinearRegression

# ------------------------------------------------------------
linear_model = LinearRegression()

# ------------------------------------------------------------
linear_model.fit(X, y)

# ------------------------------------------------------------
y_pred_linear = linear_model.predict(X)

# ------------------------------------------------------------
y_pred_linear

# ------------------------------------------------------------
plt.scatter(X, y)
plt.plot(X, y_pred_linear,color='red')
plt.title("Linear Regression - Position Level vs Salary")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# ------------------------------------------------------------
from sklearn.preprocessing import PolynomialFeatures

# ------------------------------------------------------------
poly_model = PolynomialFeatures(degree=4)

# ------------------------------------------------------------
X_poly = poly_model.fit_transform(X)

# ------------------------------------------------------------
poly_model = LinearRegression()

# ------------------------------------------------------------
poly_model.fit(X_poly, y)

# ------------------------------------------------------------
poly_model.score(X_poly,y)

# ------------------------------------------------------------
plt.scatter(X, y)
plt.plot(X,poly_model.predict(X_poly),color='red')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.title('Polynomial Regression')
plt.show()

# ------------------------------------------------------------
from sklearn.metrics import mean_squared_error, r2_score

# ------------------------------------------------------------
y_pred_poly = poly_model.predict(X_poly)

# ------------------------------------------------------------
mse = mean_squared_error(y, y_pred_poly)
r2 = r2_score(y, y_pred_poly)

# ------------------------------------------------------------
mse

# ------------------------------------------------------------
r2

# ------------------------------------------------------------
new_level = [[6.5]]

prediction = poly_model.predict(
    poly.transform(new_level)
)

prediction
