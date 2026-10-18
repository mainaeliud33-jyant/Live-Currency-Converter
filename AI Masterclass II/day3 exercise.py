"""
Multi-City Passenger Transit & Currency Tool
---------------------------------------------
Validates city routes using OpenStreetMap and dynamically calculates 
passenger fares converted into global currencies via the Frankfurter API.

Usage:
    python passenger_tool.py

Requirements:
    pip install requests
    (No API Keys required!)
"""
import json
import requests


def get_city_coordinates(city):
    url = f"https://openstreetmap.org{city}&format=json&limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_currency_conversion(amount, target_currency):
    url = f"https://frankfurter.dev{amount}&from=USD&to={target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    return None

def calculate_base_usd_fare(lat, lon, passengers, travel_class):
    """Calculates baseline travel costs locally using distance geometry vectors."""
    origin_lat, origin_lon = -1.2921, 36.8219  # Nairobi center point anchor
    distance_proxy = ((float(lat) - origin_lat)**2 + (float(lon) - origin_lon)**2)**0.5


def save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

def run_tool():
    print("=========================================")
    print("  PASSENGER ROUTE & FARE CALCULATOR  ")
    print("=========================================\n")

    city = input("Enter destination city name: ").strip()
    if not city:
        print(" Error: City name cannot be blank. Exiting.")
        return

    passengers = int(input("Enter number of passengers: "))
    if passengers <= 0:
        print(" Error: Must be at least 1 passenger.")
        return

    travel_class = input("Enter travel class (Economy / First): ").strip()
    target_curr = input("Convert final fare to which currency code? (e.g., KES, EUR, GBP, USD): ").strip().upper()

    print(f"\nConnecting to live networks to compile profiles for {city.title()}...")

    geo_data = get_city_coordinates(city)
    if not geo_data:
        print(f" Error: Could not verify location paths for '{city}'. Check spelling.")
        return

    lat = geo_data["lat"]
    lon = geo_data["lon"]

    usd_fare = calculate_base_usd_fare(lat, lon, passengers, travel_class)

    currency_data = get_currency_conversion(usd_fare, target_curr)

    combined_response = {
        "search_parameters": {"city": city, "passengers": passengers, "class": travel_class},
        "api_1_location_metadata": geo_data,
        "api_2_currency_rates": currency_data if currency_data else "Conversion Service Unavailable",
        "final_fare_usd": usd_fare
    }

    print("\n-----------------------------------------")
    print(f" TRANSIT DOSSIER: {city.upper()}")
    print("-----------------------------------------")
    print(f" Full Destination : {geo_data['display_name']}")
    print(f" Passenger Tickets: {passengers} allocated ({travel_class.title()})")
    print(f" Base Fare Cost   : ${usd_fare:,.2f} USD")

    if currency_data:
        converted_fare = currency_data["rates"][target_curr]
        print(f"Exchanged Fare   : {converted_fare:,.2f} {target_curr}")
    print("-----------------------------------------")

    filename = f"{city.lower().replace(' ', '_')}_transit_profile.json"
    save_to_file(combined_response, filename)
 

run_tool()