import requests

# 1. Open-Meteo URL (No API key needed!)
# This requests the current temperature and wind speed
url = "https://open-meteo.com"

print("Connecting to Open-Meteo...")
response = requests.get(url)

print("Status code:", response.status_code)

if response.status_code == 200:
    # 2. Parse the clean JSON response safely
    data = response.json()
    
    # 3. Extract the current weather dictionary
    current_weather = data.get("current", {})
    
    temperature = current_weather.get("temperature_2m")
    wind_speed = current_weather.get("wind_speed_10m")
    time_checked = current_weather.get("time")
    wind_direction = current_weather.get("wind_direction_10m")
    
    # 4. Extract unit measurements
    units = data.get("current_units", {})
    temp_unit = units.get("temperature_2m", "°C")
    wind_unit = units.get("wind_speed_10m", "km/h")

    print("\n--- Current Weather ---")
    print(f"Time checked: {time_checked}")
    print(f"Temperature: {temperature}{temp_unit}")
    print(f"Wind Speed: {wind_speed} {wind_unit}")
    print(f"Wind direction: {wind_direction}")
else:
    print("Failed to get weather data. Status:", response.status_code)