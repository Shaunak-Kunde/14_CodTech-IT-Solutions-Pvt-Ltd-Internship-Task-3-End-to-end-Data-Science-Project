from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# --- Load Model and Encoders ---
try:
    # Load the trained model
    model = joblib.load('power_outage_classifier.pkl')

    # Load and combine the datasets to fit the LabelEncoders
    may_path = "C://Users//kunde//Desktop//Virtual internship//CodTech IT Solutions Pvt Ltd//CodTech IT Solutions Pvt Ltd Internship//Task-3 End to end Data Science Project//Goa Power Outage Report May 2025.xlsx"
    june_path = "C://Users//kunde//Desktop//Virtual internship//CodTech IT Solutions Pvt Ltd//CodTech IT Solutions Pvt Ltd Internship//Task-3 End to end Data Science Project//Goa Power Outage Report June 2025.xlsx"
    
    df_may = pd.read_excel(may_path)
    df_june = pd.read_excel(june_path)
    df_combined = pd.concat([df_may, df_june], ignore_index=True)

    # Clean up column names by stripping whitespace
    df_combined.columns = df_combined.columns.str.strip()

    # The column name in the Excel file is "Rural/Urban"
    columns_to_rename = {
    'Town Name': 'Town_Name',
    'Substation': 'Substation',
    'Feeder Name': 'Feeder_Name',
    'Rural/Urban': 'Rural_Urban' 
    }
    
    # Check if the columns exist before renaming
    for old_name, new_name in columns_to_rename.items():
        if old_name in df_combined.columns:
            df_combined.rename(columns={old_name: new_name}, inplace=True)
            
    # Now, fit the encoders on the cleaned column names
    le_town = LabelEncoder().fit(df_combined['Town_Name'])
    le_substation = LabelEncoder().fit(df_combined['Substation'])
    le_feeder = LabelEncoder().fit(df_combined['Feeder_Name'])
    le_rural_urban = LabelEncoder().fit(df_combined['Rural_Urban'])

except Exception as e:
    print(f"Error during initialization: {e}")
    print("Please ensure your Excel column names are exactly correct and the file paths are valid.")
    exit()

# --- Endpoint to get dropdown options ---
@app.route('/get_options', methods=['GET'])
def get_options():
    try:
        substations = le_substation.classes_.tolist()
        feeders = le_feeder.classes_.tolist()
        return jsonify({
            "substations": substations,
            "feeders": feeders
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Endpoint for Predictions ---
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_df = pd.DataFrame([data])
        
        # Transform the incoming data using the pre-fitted encoders
        input_df['Town_Name_Encoded'] = le_town.transform(input_df['Town Name'])
        input_df['Substation_Encoded'] = le_substation.transform(input_df['Substation'])
        input_df['Feeder_Name_Encoded'] = le_feeder.transform(input_df['Feeder Name'])
        input_df['Rural_Urban_Encoded'] = le_rural_urban.transform(input_df['Rural/Urban'])
        
        features = ['Town_Name_Encoded', 'Substation_Encoded', 'Feeder_Name_Encoded', 'Rural_Urban_Encoded']
        prediction = model.predict(input_df[features])[0]
        result = 'Long Outage (> 1 hour)' if prediction == 1 else 'Short Outage (<= 1 hour)'
        
        return jsonify({'predicted_outage_category': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)