import json

# Different system prompts produce different outputs for the same user message
system_prompts = {
    "SMP Coach": (
        "You are a strict SMP fitness coach. Be direct, no fluff. "
        "Give one actionable recommendation per response. Max 3 sentences."
    ),
    "Data Analyst": (
        "You are a fitness data analyst. Focus on numbers and trends. "
        "Output structured observations, not advice."
    ),
    "Nutritionist": (
        "You are a nutritionist specializing in intermittent fasting protocols. "
        "Focus only on eating patterns and timing."
    )
}

user_message = "James: steps=7800, sleep=6hr, protocol=OMAD, water=5 glasses, day 3 of deficit."

# Simulated responses for each system prompt
simulated_responses = {
    "SMP Coach": (
        "Six hours of sleep on day 3 of a deficit is why the steps are low. "
        "Tonight, sleep must be 8+ hours. Tomorrow target 9,000 steps only."
    ),
    "Data Analyst": (
        "Observation: Steps 22% below 10k goal. Sleep deficit likely compounding protocol fatigue. "
        "Water intake at 5/8 target. Recommend tracking energy levels as a leading indicator."
    ),
    "Nutritionist": (
        "Day 3 of OMAD with sleep deficit suggests cortisol is elevated. "
        "Consider shifting to 2MAD tomorrow to reduce stress load and support recovery."
    )
}

for role, prompt in system_prompts.items():
    print(f"[{role}]")
    print(f"  System: {prompt[:60]}...")
    print(f"  Response: {simulated_responses[role]}")
    print()