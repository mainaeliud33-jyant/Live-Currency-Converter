# Simulates the object that response.choices[0].message.content extracts from
# This mirrors the actual OpenAI API response structure exactly

class Message:
    def __init__(self, content):
        self.content = content
        self.role = "assistant"

class Choice:
    def __init__(self, content):
        self.message = Message(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [Choice(content)]
        self.model = "gpt-4o-mini"
        self.usage = {"prompt_tokens": 45, "completion_tokens": 82, "total_tokens": 127}

# Simulated response as if the API returned it
sim_response = SimulatedResponse(
    "Sleep was the limiting factor today. James hit 7,800 steps but 6 hours is below optimal. "
    "Tomorrow: prioritize 8+ hours tonight. Keep the step target at 9,000, not 10,000, "
    "since recovery is still incomplete. Add a 20-minute walk after lunch to hit it without needing a long session."
)

# Extract the reply (same code you use with the live API)
reply = sim_response.choices[0].message.content
print("AI Coach Response:")
print(reply)
print(f"\nTokens used: {sim_response.usage['total_tokens']}")