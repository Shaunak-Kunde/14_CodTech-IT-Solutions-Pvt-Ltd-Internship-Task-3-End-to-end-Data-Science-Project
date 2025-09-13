# CODTECH Internship – Task 3: Goa Power Outage Prediction ⚡

This project is part of my CODTECH Virtual Internship under Data Science. The goal is to build a full Data Science pipeline, from data collection and preprocessing to model training and deployment using FastAPI, to predict power outages in Goa. I have also included a short demo video showing the API in action.

# Goa Power Outage Prediction

This project implements a Random Forest model to classify power outages into:

Short Outage (≤ 1 hour)

Long Outage (> 1 hour)

based on historical data from the Goa Power Outage Report May 2025.xlsx. The trained model is deployed as a FastAPI API, allowing users to get real-time predictions by sending JSON data. This is my FastAPI deployment for ML, after experimenting with Streamlit, Flask, joblib, and pickle.

# 🚀 Project Workflow
Dataset Access

Dataset: Goa Power Outage Report May 2025 (available on Goa Electricity Dept Website)

Columns: Town Name, Substation, Feeder Name, Rural/Urban, No of Consumers, No of Outages, Duration of Outage, Average Hours of Steady Supply

Only May 2025 data is used for this project.

# Data Preprocessing

Cleaned column names and removed extra spaces.

Handled missing numeric values by replacing NaN with 0.

Converted categorical columns (Town_Name, Substation, Feeder_Name, Rural_Urban) into numerical features using LabelEncoder.

Defined the target variable Outage_Category:

0 → Short Outage (≤ 1 hour)

1 → Long Outage (> 1 hour)

# Model Development

# Algorithm: Random Forest Classifier

Features: Town_Name, Substation, Feeder_Name, Rural/Urban, No_of_Consumers

Train/Test Split: 80/20

Evaluated using accuracy and classification report.

Model & encoders saved using Joblib (model.pkl & encoders.pkl).

# FastAPI Deployment

API Endpoint: POST /predict

Input JSON Example:

{
  "Town_Name": "MAPUSA",
  "Substation": "33KV Nagoa",
  "Feeder_Name": "11KV Arpora",
  "Rural_Urban": "RURAL",
  "No_of_Consumers": 2209
}


Output Example:

{
  "prediction": "Short Outage (<= 1 hour)"
}


# Local Deployment: Runs on http://127.0.0.1:8000/
<img width="857" height="391" alt="image" src="https://github.com/user-attachments/assets/a10e04b9-2aba-41e0-9637-0beef0cac593" />
Interactive Docs: http://127.0.0.1:8000/docs
<img width="865" height="385" alt="image" src="https://github.com/user-attachments/assets/82297900-61c2-4bf0-856c-5f6923768ab9" />


# Exploratory Data Analysis & Visualizations

Bar Chart: Top towns by total number of outages.

Scatter Plot: Correlation between outage duration and number of outages.

Pie Chart: Distribution of consumers in Rural vs Urban areas.

Line Chart: Total outages by town for May 2025.

Bar Charts: Top 5 reasons for outages in May.

Bar Chart: Top 10 substations by total outage duration.

These visualizations provide insights into outage distribution and help in understanding the dataset before deployment.

# 🛠️ Tools & Libraries

Python 3.10+

FastAPI – API deployment

Uvicorn – ASGI server

Pandas & NumPy – Data manipulation

Scikit-learn – Model development

Matplotlib & Seaborn – Visualization

Joblib – Saving models and encoders

📂 Project Structure
Task-3 Goa Power Outage Project/
│── Goa Power Outage Report May 2025.xlsx
│── train.ipynb
│── main.py
│── model.pkl
│── encoders.pkl
│── requirements.txt
│── readme.md
│── short demo end to end data science using fastAPI.mp4

# ✅ Summary & Insights

Data preprocessing and encoding ensure that the model handles new inputs via API.

Random Forest performs robustly on small tabular datasets for outage prediction.

FastAPI deployment allows real-time predictions with a simple POST request.

Visualizations provide insights into power outage trends across towns and substations in May 2025.

# A short demo video is included to showcase API functionality.

⚠️ Notes

Only May 2025 data is used; additional months can be added for future extensions.

Ensure model.pkl and encoders.pkl are present to run the FastAPI app.

Start the API using:

uvicorn main:app --reload --port 8000


# 👨‍💻 Developed by: Shaunak Damodar Sinai Kunde

