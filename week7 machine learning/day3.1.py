#A Reusable Prediction Function
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Train
X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps_y = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y = (steps_y >= 10000).astype(int)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X, y)

# Reusable function
def predict_day(sleep_hours, water_glasses, bench_kg):
    """
    Predict whether today will be a 10k step day.
    Returns: dict with prediction, confidence, and recommendation.
    """
    inputs = np.array([[sleep_hours, water_glasses, bench_kg]])
    pred = clf.predict(inputs)[0]
    proba = clf.predict_proba(inputs)[0]
    confidence = max(proba)

    result = {
        "hit_goal": bool(pred),
        "confidence": round(confidence * 100, 1),
        "recommendation": ""
    }

    if pred == 0 and confidence > 0.7:
        result["recommendation"] = "Low step day likely. Schedule a walk this afternoon."
    elif pred == 1 and confidence > 0.7:
        result["recommendation"] = "High step day likely. Good conditions today."
    else:
        result["recommendation"] = "Borderline day. Stay intentional about movement."

    return result

# Test with three different days
scenarios = [
    (8.0, 8, 84, "James Omondi"),
    (6.0, 5, 78, "Brian Kamau"),
    (9.0, 9, 87, "Grace Achieng"),
    (6.0, 5, 60, "Irimu Maina"),
]

for sleep, water, bench, name in scenarios:
    r = predict_day(sleep, water, bench)
    outcome = "Goal hit" if r["hit_goal"] else "Below goal"
    print(f"{name}: {outcome} ({r['confidence']}% confidence)")
    print(f"  {r['recommendation']}")
    print()