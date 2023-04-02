import requests
import json
from datetime import datetime, timedelta

# Define a function to get weather data for a city from OpenWeatherMap API
def get_weather_data(city_name, num_days, api_key):
    # Set up API endpoint URL with city name, number of days to predict, and API key
    url = "https://api.openweathermap.org/data/2.5/forecast?q=" + city_name + "&cnt=" + str(num_days * 8) + "&appid=" + api_key
    # Send API request and get response
    response = requests.get(url)
    # Convert JSON response to dictionary
    data = json.loads(response.text)
    # Return dictionary
    return data

# Define a function to extract relevant weather data from API response
def extract_weather_data(data, num_days):
    # Create empty list to store weather data
    weather_data = []
    # Loop through each day of the forecast
    for i in range(num_days):
        # Get date of current day
        date = (datetime.today() + timedelta(days=i)).strftime('%Y-%m-%d')
        # Loop through each 3-hour interval of the day (8 intervals per day)
        for j in range(8):
            # Get time of current interval
            time = data['list'][j+(i*8)]['dt_txt']
            # Get temperature in Kelvin and convert to Celsius
            temperature = data['list'][j+(i*8)]['main']['temp'] - 273.15
            # Get humidity as a percentage
            humidity = data['list'][j+(i*8)]['main']['humidity']
            # Get weather description
            description = data['list'][j+(i*8)]['weather'][0]['description']
            # Add weather data to list as a dictionary
            weather_data.append({'date': date, 'time': time, 'temperature': temperature, 'humidity': humidity, 'description': description})
    # Return list of weather data dictionaries
    return weather_data

# Get user input for city name and number of days to predict
city_name = input("Enter city name: ")
num_days = int(input("Enter number of days to predict: "))

# Set up OpenWeatherMap API key
api_key = "b72af671ed2dda3965c6fb38d7a52768"

# Get weather data from API and extract relevant data
data = get_weather_data(city_name, num_days, api_key)
weather_data = extract_weather_data(data, num_days)

# Print weather data for each day
for i in range(num_days):
    # Get date of current day
    date = (datetime.today() + timedelta(days=i)).strftime('%Y-%m-%d')
    print("Weather predictions for", date)
    # Loop through weather data and print data for current day
    for weather in weather_data:
        if weather['date'] == date:
            print(weather['time'], "-", weather['description'], "-", "Temperature:", round(weather['temperature'], 1), "°C", "Humidity:", weather['humidity'],"%")
    print("\n")
