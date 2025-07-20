
import streamlit as st
import pandas as pd
import joblib
import os

# Function to load the trained model (runs once)
@st.cache_resource
@st.cache_resource
def load_model():
    return joblib.load(r'C:\Users\HP\Desktop\energy\appliance_energy_rf.joblib')

model = load_model()

# Streamlit App Title and Instructions
st.title("Appliance Energy Usage Predictor")

st.write(
    "Upload a CSV file with the same columns used for model training (excluding 'Appliances' and 'date'). "
    "The app will generate appliance energy usage predictions for each row."
)

# File uploader for user input
uploaded_file = st.file_uploader(
    "Choose a CSV file to upload",
    type=["csv"],
    help="Your input file should match the features used in training, without columns 'Appliances' and 'date'."
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Drop unnecessary columns if present
    columns_to_remove = [col for col in ['Appliances', 'date'] if col in df.columns]
    df = df.drop(columns=columns_to_remove, axis=1, errors='ignore')

    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    # Generate predictions
    predictions = model.predict(df)

    st.subheader("Predicted Appliance Energy Usage (Wh)")
    prediction_df = pd.DataFrame({"Predicted Energy (Wh)": predictions})
    st.dataframe(prediction_df.head())

    # Combine input and predictions for download
    output = df.copy()
    output["Predicted Appliances Energy (Wh)"] = predictions
    st.download_button(
        label="Download Predictions as CSV",
        data=output.to_csv(index=False),
        file_name="energy_predictions.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload a CSV file to get predictions.")

st.markdown("---")
st.markdown("Made by Kanika Katare")
