
import numpy as np
​
def greatest_impact(lst):
    factors = ["Weather", "Meals", "Sleep"]
    max_val = [10, 3, 10]
    scores = [[],[],[]]
    for part in lst:
        for i in range(1, len(part)):
            scores[i-1].append(part[0] / (part[i] / max_val[i-1]))
    mean = np.array(scores).mean(axis=1)
    if np.max(mean) == np.min(mean):
        return "Nothing"
    return factors[mean.argmax()]

