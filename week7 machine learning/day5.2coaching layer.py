


# Simulated coaching layer
# The response structure mirrors the OpenAI API object
class SimulatedMessage:
    def __init__(self, content):
        self.content = content

class SimulatedChoice:
    def __init__(self, content):
         self.message = SimulatedMessage(content)

class SimulatedResponse:
     def __init__(self, content):
         self.choice = [SimulatedChoice(content)]
         
COACHING_TEMPLATES = {
     # key: (hit_goal, sleep_ok, water_ok)
     (True, True, True): ("Strong input, strong output. Sleep and hydration are locked.", 
                          "keep this baseline consistent, steps will follow."),
     (True, True, False): ("You hit the goal despite low water. Sleep is your biggest lever.", 
                           "Push the hydration tomorrow and the margin grows."),
     (True, False, True): ("Water carried today's performance despite low sleep.", 
                           "Shore up sleep tonigt. Hitting goals on low sleep has hidden costs."),
     (True, False, False): ("Goal hit through willpower, not system. Willpower can run out.", 
                            "Fix sleep and water before the next session."),
     (False, True, True): ("Inputs were solid but the goal was missed.", 
                           "Audit what absorbs the energy. Do not cut sleep and water."), 
     (False, True, False): ("Sleep is solid, hydration is low, goal missed.",  
                            "Add two glasses of water tomorrow, hydration shifts step count more than expected."),
     (False, False, True): ("Low sleep is the lead Variable. Water is fine.", 
                            "Get to bed 45 minute earler. The effect shows in 72 hours."),
     (False, False, False): ("Both inputs are below threshhold. Goal was missed.", 
                             "Reset tonight 8hrs sleep and 10 water glasses tomorrow."),
     }

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    """Simulated coaching. Real version calls OpenAI Chat API."""
    sleep_ok = sleep >= 7.0
    water_ok = water >= 8
    key = (bool(hit_goal),sleep_ok, water_ok)
    line1, line2 = COACHING_TEMPLATES[key]
    coaching_text = f"{line1} {line2}"
    return SimulatedResponse(coaching_text)

# Test the coaching layer directly
test_cases = [
    (8.0, 10, 90, True,  0.91),
    (5.5, 4,  70, False, 0.88),
    (7.5, 6,  85, True,  0.74),
]

for sleep, water, bench, hit, conf in test_cases:
    response = get_coaching_message(sleep, water, bench, hit, conf)
    message = response.choice[0].message.content
    outcome = "HIT GOAl" if hit else "GOAL MISSED"
    print(f"[{outcome}  | {conf:.0%} confidence]")
    print(f"Sleep {sleep}h | Water {water} glasses | bench {bench}kg")
    print(f"coach: {message}")
    print("-" * 60)