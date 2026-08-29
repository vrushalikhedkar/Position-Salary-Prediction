# Position-Salary-Prediction

## 🛠️ Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook


## Project Overview

A Machine Learning project that predicts **salary based on position level**.

- **Type:** Supervised Learning
- **Problem:** Regression
- **Input (X):** Level
- **Target (y):** Salary
- **Models:** Linear Regression & Polynomial Regression
- **Polynomial Degree:** 4


<p align="center">
  <img src="Position_Salary_Prediction_Final_Infographic_Under_1MB.jpg" width="1000">
</p>


## 📂 Dataset

**Dataset:** `Position_Salaries.csv`

| Feature | Description |
|---|---|
| Position | Employee Designation |
| Level | Newmerical Position Level |
| Salary | Target Salary |


```text
X = Level
y = Salary 
```

## 🔎 EDA

The dataset was analyzed using:
- Dataset inspection
- info()
- describe()
- Missing value check
- Scatter plot

Observation
- Salary increases with position level.
- Salary growth is not constant.
- The relationship is non-linear.

## 📈 Linear Regression

Linear Regression was used as a baseline model.
 
```test
y = mx + c
```

It represents the relationship using a straight line.

## 🧠 Polynomial Regression

Because the relationship is non-linear, Polynomial Regression was used.

For degree 4:

```text
Level
Level²
Level³
Level⁴
```

**Why Polynomial Regression?**
- Captures non-linear relationships
- Fits the salary pattern better
- Performs better than Linear Regression on this dataset

## 📊 Model Evaluation

**Polynomial Regression Results**
- MSE: ```210,343,822.84```
- R² Score: ```0.99739```

**Lower MSE = Better**<br/>
**Higher R² = Better**

## 🔮 Prediction

For:

```text
Position Level = 6.5
```
**Predicted Salary**<br/>
**₹158,862.45 approximately**

## 🏆 Final Result

**Best Model:** Polynomial Regression<br/>
**Degree:** 4<br/>
**R² Score:** 0.99739<br/>
**Predicted Salary:** ₹158,862.45<br/>


**Polynomial Regression was more suitable because the relationship between position level and salary is non-linear.**

