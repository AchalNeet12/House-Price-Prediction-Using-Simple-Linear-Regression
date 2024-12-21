# **House Price Prediction**
---

## Overview
This project is a House Price Prediction App built using Streamlit and Simple Linear Regression. The app predicts the price of a house based on the square footage of the living area. It leverages a machine learning model trained on a dataset of house prices and features a user-friendly interface for input and output.

---

##  Simple Linear Regression
Simple Linear Regression is a statistical method to find the relationship between two variables:
- Independent Variable (X): The input (e.g., square footage).
- Dependent Variable (y): The output (e.g., house price).

Equation:
          y=mx+c

Where:

- m: Slope of the line (how much y changes for a unit change in X).
- c: Intercept (value of y when X = 0).
- **Role of Simple Linear Regression in the Project**
  Purpose: Establishes a linear relationship between square footage and house price.
  Training: The model learns parameters m and 𝑐 from the training data.
  Prediction: For any given square footage, the model predicts the house price using the learned equation.
  By using simple linear regression, the app provides an easy-to-understand prediction mechanism while keeping the implementation straightforward and interpretable.

---

## Dataset
- **Source:** The dataset used is the Salary_Data.csv file (should be replaced with a housing dataset).
- **Features:**
  **Independent Variable (X):** Square footage of the living area.
  **Dependent Variable (y):** House price.
- **Structure:**
  **Rows:** Data points (examples of houses).
  **Columns:** Feature (square footage) and target (price).

---

## Data Preprocessing Steps
1. **Data Loading:**
   Read the CSV file containing house price data.
   Extract the independent (X) and dependent (y) variables.
2. **Data Splitting:**
   Split the data into training and testing sets (80% training, 20% testing) using train_test_split.
3. **Scaling/Transformation:**
   For simple linear regression, scaling is not required unless the data values have extremely large ranges.
4. **Model Training:**
   Fit a linear regression model on the training data using LinearRegression.fit().

---
   
## Features
- **Input:** Users provide square footage of the living area as input.
- **Output:** The app predicts the estimated house price based on the input.
- **Model Training:** Uses simple linear regression to establish a relationship between square footage and house price.
- **Background Design:** Customizable visual appearance with a background image.

---

## Technology Used
1. **Programming Language:**
  - Python
2. **Framework:**
  - Streamlit: For creating the web app interface.
3 **Libraries:**
  - NumPy: For numerical computations.
  - Pandas: For data manipulation.
  - Scikit-learn: For building and evaluating the regression model.
  - Base64: For encoding the background image.
  - Streamlit Styling: For customizing the app layout and appearance.

---

## Results
The model predicts house prices based on square footage.

---

## Conclusion
The project successfully demonstrates how simple linear regression can be applied to predict house prices. The app is interactive and provides predictions based on user input. While simple, this model can serve as a foundation for more complex prediction systems.




