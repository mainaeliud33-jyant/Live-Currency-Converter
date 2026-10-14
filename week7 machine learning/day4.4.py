import json

# System prompt requesting JSON output
system = """You are a fitness data extractor.
Parse the user's daily log and return ONLY valid JSON with these keys:
steps (int), sleep_hours (float), protocol (str), cold_shower (bool), water_glasses (int).
No other text."""

# What the AI would return for this input
raw_log = "Today I did 3,890 steps, slept for 6.5 hours, followed 2MAD, took a cold shower and drank 3 glasses of water."

# Simulated AI JSON response
simulated_json_response = '{"steps": 3890, "sleep_hours": 6.5, "protocol": "2MAD", "cold_shower": true, "water_glasses": 3}'

# Parse it
try:
    parsed = json.loads(simulated_json_response)
    print("Parsed structured data:")
    for key, value in parsed.items():
        print(f"  {key}: {value}")

    # Use it programmatically
    print()
    if parsed["steps"] >= 10000:
        print("Step goal: HIT")
    else:
        print(f"Step goal: {parsed['steps']:,}/10,000 ({10000 - parsed['steps']:,} short)")
    print(f"Sleep rating: {'Good' if parsed['sleep_hours'] >= 7.5 else 'Low'}")

except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e}")