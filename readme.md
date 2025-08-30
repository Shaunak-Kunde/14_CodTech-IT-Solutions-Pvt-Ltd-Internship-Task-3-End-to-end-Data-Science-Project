# CODTECH Internship – Task 3: End-to-End Data Science Project
This project is part of my CODTECH Virtual Internship under Data Science.
The goal is to develop an end-to-end data science project, from data collection and preprocessing to model deployment using Flask.

# Goa Power Outage Predictor ⚡
This project implements a supervised machine learning model (Random Forest Classifier) to predict the category of power outages (short or long duration) in different parts of Goa, India. The project includes data cleaning, model training, and deployment as a web application.

# 🚀 Project Workflow
1. Data Collection and Preprocessing
Dataset: Power outage reports for May and June 2025, provided in two Excel files (Goa Power Outage Report May 2025.xlsx and Goa Power Outage Report June 2025.xlsx). This is public data available at https://www.goaelectricity.gov.in/Home_page.aspx

Preprocessing: The datasets were combined, and categorical features such as 'Town Name', 'Substation', 'Feeder Name', and 'Rural/Urban' were cleaned and encoded using LabelEncoder to prepare them for the model.

2. Model Development
A machine learning classifier was trained on the preprocessed data to predict the likelihood of a power outage being either a 'Short Outage (<= 1 hour)' or a 'Long Outage (> 1 hour)'.

The trained model was saved as a serialized file, power_outage_classifier.pkl, for easy deployment.

3. API & Web Application Deployment
Flask API: A Flask backend was created with two main API endpoints:

/get_options: Fetches unique values for substations and feeder names to populate the dropdown menus on the web page.

/predict: Accepts user input and uses the loaded machine learning model to return a prediction.

Web App: An index.html file serves as the front-end user interface. It allows users to select town, substation, feeder, and area type. It then sends this data to the Flask API to get and display a real-time prediction.

🛠️ Tools & Libraries
Python 3.10+

Flask – The web framework used for API development.

pandas – For data manipulation and preprocessing.

scikit-learn – For LabelEncoder and the machine learning model.

joblib – To save and load the trained model.

HTML, CSS, JavaScript – For the front-end web interface.

📂 Project Structure
Task-3 End-to-End Data Science Project/
│── Goa Power Outage Report May 2025.xlsx    # Raw data
│── Goa Power Outage Report June 2025.xlsx   # Raw data
│── power_outage_classifier.pkl                # Trained model
│── app.py                                     # Flask backend
│── index.html                                 # Front-end web page
│── readme.md                                  # Project documentation
│── reqirements.txt                            # necessary libraries

✅ Deliverables
A deployed web application that provides real-time predictions for power outages.

Trained machine learning model saved as power_outage_classifier.pkl.

Source code for the Flask API and the front-end interface.

This concludes Task 3: End-to-End Data Science Project for the CodTech Internship 🚀

👨‍💻 Developed by: Shaunak Damodar Sinai Kunde

