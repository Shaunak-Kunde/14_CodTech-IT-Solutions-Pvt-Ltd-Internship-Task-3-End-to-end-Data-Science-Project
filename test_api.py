import requests
import json

# The data you want to send for a prediction
data = {
    "No_of_Consumers": 500,
    "Town Name": "VASCO",
    "Substation": "33KV Substation A",
    "Feeder Name": "11KV Feeder A",
    "Rural / Urban": "URBAN"
}

# The URL of your API endpoint
url = "http://127.0.0.1:5000/predict"

# Send the POST request
response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Print the response from the server
print(response.json())