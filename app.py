import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the saved model pipeline
model_path = "catboost_model_pipeline.pkl"

with open(model_path, "rb") as model_file:
    pipeline = pickle.load(model_file)

# Feature info
numeric_features_info = {
    'Annual_Income': (5000, 30000000),
    'Monthly_Inhand_Salary': (100, 2500000),
    'Num_Bank_Accounts': (0, 20),
    'Num_Credit_Card': (0, 15),
    'Interest_Rate': (1, 100),
    'Num_of_Loan': (0, 20),
    'Delay_from_due_date': (0, 70),
    'Num_of_Delayed_Payment': (0, 100),
    'Changed_Credit_Limit': (-10.0, 40.0),
    'Num_Credit_Inquiries': (0, 50),
    'Outstanding_Debt': (0, 5000),
    'Credit_Utilization_Ratio': (0, 100),
    'Total_EMI_per_month': (0, 82330),
    'Amount_invested_monthly': (0, 10000),
    'Monthly_Balance': (0, 1600),
    'Credit_History_Age_in_Months': (1, 404),
    'Age': (18, 100),
}

occupation_options = [
    'Accountant', 'Architect', 'Developer', 'Doctor', 'Engineer',
    'Entrepreneur', 'Journalist', 'Lawyer', 'Manager', 'Mechanic',
    'Media_Manager', 'Musician', 'Scientist', 'Teacher', 'Writer', "Other"
]

loan_types = [
    'Auto Loan', 'Credit-Builder Loan', 'Personal Loan', 'Home Equity Loan',
    'Payday Loan', 'Student Loan', 'Mortgage Loan', 'Not Specified'
]

# Streamlit UI
st.title("Credit Score Prediction App")
st.write("Enter the required details to predict the credit score category.")

user_input = {}

# Numeric inputs
for col, (min_val, max_val) in numeric_features_info.items():
    default_val = round((min_val + max_val) / 2, 1) if isinstance(min_val, float) or isinstance(max_val, float) else (min_val + max_val) // 2
    label = f"{col} (Range: {min_val} - {max_val})"
    user_input[col] = st.number_input(
        label,
        min_value=min_val,
        max_value=max_val,
        value=default_val  # Set default value to mid-range
    )

# Occupation dropdown
user_input['Occupation'] = st.selectbox("Occupation", occupation_options, index=0)

# Loan types multiselect
selected_loans = st.multiselect("Type of Loan (Select one or more)", loan_types)
user_input['Type_of_Loan'] = ", ".join(selected_loans) if selected_loans else ""

# Predict
if st.button("Predict Credit Score"):
    # Make sure that no missing values are present (ensure all inputs are numeric or categorical)
    input_df = pd.DataFrame([user_input])

    # Check for missing data
    if input_df.isnull().sum().any():
        st.error("Please ensure all fields are filled.")
    else:
        # Make prediction using the trained pipeline
        prediction_proba = pipeline.predict_proba(input_df)

        # Get class labels
        class_labels = pipeline.named_steps['classifier'].classes_

        # Display the probability for each class
        st.write("### Prediction Probabilities:")
        for label, prob in zip(class_labels, prediction_proba[0]):
            st.write(f"**{label}:** {prob:.2%}")

        # Show the most likely credit score category
        predicted_class = class_labels[np.argmax(prediction_proba)]
        st.success(f"Predicted Credit Score: **{predicted_class}**")
