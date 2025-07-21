# Appliance Energy Usage Predictor

This is a web-based tool built using Streamlit to predict appliance energy usage (in Wh) from sensor data using a pre-trained machine learning model.

## 📁 Project Structure

.
├── f1.py # Streamlit app for predictions
├── appliance_energy_rf.joblib # Pre-trained Random Forest model (place this in the same folder)
├── requirements.txt # Required Python packages
└── README.md # Setup and usage guide

2. Create a Virtual Environment
Using venv:
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

Using pipenv:
pip install pipenv
pipenv shell

3. Install Required Packages
pip install -r requirements.txt

🚀 Running the App
Make sure appliance_energy_rf.joblib is in the same directory as f1.py.
streamlit run f1.py

📤 Using the App
Upload a CSV file that matches the training feature set (excluding 'Appliances' and 'date').
View the preview of uploaded data.
See predictions for each row in the file.
Download results as a CSV.

📎 Notes
Ensure your CSV has only the features used during model training.
The pre-trained model is a Random Forest Regressor trained to predict appliance energy consumption.
You can retrain the model using any regression algorithm (e.g., RandomForest, GradientBoost, etc.) using the same dataset format and save it using joblib.




