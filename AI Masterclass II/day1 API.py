import requests

country = "Kenya"

# Fixed URL string with explicit structural forward slashes
url = f"https://restcountries.com{country}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        # The API returns data wrapped inside a list: [ {...} ]
        data = response.json()[0] 
        
        official_name = data["name"]["official"]
        # Capital is provided as a list, grab the first element
        capital = data["capital"][0] if "capital" in data else "N/A"
        population = data["population"]
        
        print(f"Data for {country}:")
        print(f"- Official Name: {official_name}")
        print(f"- Capital City: {capital}")
        print(f"- Population: {population:,}")

    elif response.status_code == 404:
        print(f"Country not found: {country}")
    else:
        print(f"Unexpected error: {response.status_code}")

except requests.exceptions.ConnectionError as e:
    print("❌ Network Error: Failed to resolve the web address.")
    print(f"Details: {e}")