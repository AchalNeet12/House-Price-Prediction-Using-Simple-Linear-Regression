# Import Libraries
import numpy as np
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import base64

# Function to set background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: white; /* Set all text color to white */
    }}
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
        color: white; /* Ensure headers are also white */
    }}
    .stSidebar .sidebar-content {{
        background-color: rgba(0, 0, 0, 0.5); /* Optional: change sidebar background to semi-transparent black */
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call the function to set the background (you need to provide the correct image path)
set_background("th.jpg")

# Load Dataset
def load_data():
    try:
        # Update the path to your CSV file
        dataset = pd.read_csv(r"House_data.csv")
        X = dataset[['sqft_living']]  # Ensure X is 2D
        y = dataset['price']
        return X, y
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

# Train Model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor

# Streamlit App
st.title("🏡 House Price Prediction App")
st.write("**Predict the price of a house based on square footage of living area using a simple linear regression model.**")

# Load and Train the Model
X, y = load_data()
if X is not None and y is not None:
    model = train_model(X, y)

    # Input Section
    squarefit_living = st.number_input("Enter square footage of living area:", min_value=0.0, step=0.1, format="%.1f")

    # Prediction
    if st.button("Predict House Price"):
        try:
            predicted_price = model.predict(np.array([[squarefit_living]]))
            st.write(f"🏠 **Predicted House Price:** **${predicted_price[0]:,.2f}** for {squarefit_living:.1f} square feet of living area.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
else:
    st.warning("Unable to load data. Please check the dataset path and format.")

st.write("---")
st.write("**📈 The model was trained using a dataset of house prices and square footage of living area.**")
