import requests

# 1. This endpoint request specifically targets Kenya
url = 'https://restcountries.com'
headers = {'Authorization': 'Bearer rc_live_262af9d1a1ec4f5a858c856c89609a31'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    payload = response.json()
    
    # 2. Extract the country list from the v5 data key dictionary wrapper
    countries_list = payload.get("data", [])
    
    if countries_list:
        # Grab the first matching country array dictionary entry
        country = countries_list[0]

        # 3. Pull details using the new v5 property architecture layout
        name = country["names"]["common"]
        capital = country["capitals"][0]["name"]
        population = country["population"]
        currency = country["currencies"][0]["code"]

        print(f"Country: {name}")
        print(f"Capital: {capital}")
        print(f"Population: {population:,}")
        print(f"Currency: {currency}")
    else:
        print("No country data found in the response matching 'kenya'.")
else:
    print("Request failed. Status:", response.status_code)