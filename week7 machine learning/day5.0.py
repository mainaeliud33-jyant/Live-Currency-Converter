import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 28-day SMP training data
# Features: [sleep_hr, water_glasses, bench_kg]
X = np.array([
    [6.5, 6, 80], [7.2, 8, 85], [5.8, 5, 75], [8.0, 10, 90],
    [7.5, 9, 88], [6.0, 6, 78], [7.8, 8, 86], [8.2, 10, 92],
    [5.5, 4, 70], [7.0, 7, 82], [6.8, 8, 84], [8.5, 11, 95],
    [7.3, 9, 89], [6.2, 6, 76], [7.9, 10, 91], [5.9, 5, 73],
    [8.1, 11, 93], [7.4, 8, 87], [6.7, 7, 83], [8.3, 10, 94],
    [5.6, 4, 71], [7.1, 8, 85], [8.0, 9, 90], [6.4, 6, 77],
    [7.6, 9, 88], [8.4, 11, 96], [6.3, 7, 79], [7.7, 10, 91]
])

# Labels: 1 = hit 10,000 steps, 0 = did not
y = np.array([0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1])
