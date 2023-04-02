import requests
import json
from datetime import datetime, timedelta

# Set up OpenWeatherMap API endpoint and API key
url = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "here we have to enter api key"

# Get user input for city name and number of days to predict
city_name = input("Enter city name: ")
num_days = int(input("Enter number of days to predict: "))

# Set up API request with city name, API key, and number of days to predict
complete_url = url + "appid=" + api_key + "&q=" + city_name + "&cnt=" + str(num_days * 8)

# Send API request and get response
response = requests.get(complete_url)

# Parse JSON response
data = json.loads(response.text)

# Extract relevant weather data for each day
for i in range(num_days):
    date = (datetime.today() + timedelta(days=i)).strftime('%Y-%m-%d')
    print("Weather predictions for", date)
    for j in range(8):
        time = data['list'][j+(i*8)]['dt_txt']
        temperature = data['list'][j+(i*8)]['main']['temp']
        humidity = data['list'][j+(i*8)]['main']['humidity']
        description = data['list'][j+(i*8)]['weather'][0]['description']
        print(time, "-", description, "-", "Temperature:", temperature, "Humidity:", humidity)
    print("\n")
