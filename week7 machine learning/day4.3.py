def simulate_ai_response(messages):
    """Simulates what the OpenAI API returns based on the last user message."""
    last_user_msg = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")

    if "7800" in last_user_msg or "low" in last_user_msg.lower():
        return "Sleep was the limiter today. Prioritize 8+ hours tonight and target 9,000 steps tomorrow."
    elif "bench" in last_user_msg.lower() or "88" in last_user_msg:
        return "88kg bench on deficit sleep is strong. Deload to 80% next session to protect the joints."
    elif "protocol" in last_user_msg.lower() or "OMAD" in last_user_msg:
        return "OMAD works on high-sleep days. On sub-7 sleep, consider 2MAD to reduce cortisol load."
    else:
        return "Noted. Keep tracking and adjust the inputs. Consistency over perfection."

# Build conversation manually (what your script would maintain)
conversation = [
    {"role": "system", "content": "You are a direct SMP fitness coach. Max 2 sentences per reply."}
]

user_inputs = [
    "James hit 7800 steps today and slept 6 hours. OMAD protocol, day 3.",
    "He also hit a bench press PR of 88kg despite the deficit.",
    "Should he switch from OMAD to 2MAD tomorrow?"
]

print("=== Conversation ===\n")
for user_msg in user_inputs:
    # Add user message
    conversation.append({"role": "user", "content": user_msg})
    print(f"User: {user_msg}")

    # Simulate AI response
    reply = simulate_ai_response(conversation)

    # Add assistant reply to history
    conversation.append({"role": "assistant", "content": reply})
    print(f"Coach: {reply}\n")