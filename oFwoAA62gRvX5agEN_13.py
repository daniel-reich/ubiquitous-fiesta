
from itertools import combinations
def knapsack(size, items):
    max_value = 0
    # discard items if their weight is greater than limit
    items = [item for item in items if item["weight"] <= size]
    indices = range(len(items))
    best_indices=[]
    for n in indices:
        for i in combinations(indices, n+1):
            total_value = sum(items[p]["value"] for p in i)
            total_weight = sum(items[p]["weight"] for p in i)
            if total_value > max_value and total_weight <= size:
                max_value = total_value
                best_indices = i
    bag = [items[index] for index in best_indices]
    return {
        'capacity': size,
        'items': bag,
        'weight': sum(item["weight"] for item in bag),
        'value': sum(item["value"] for item in bag)
        }

