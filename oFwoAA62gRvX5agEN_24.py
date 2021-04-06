
def knapsack(capacity, items):
  from itertools import combinations
  
  max_value, best_weight, best_group = 0, 0, list()
  
  for n in range(1, len(items)+1):
    for group in combinations(items, n):
      weights, values = 0, 0
      for item in group:
        weights += item["weight"]
        if weights > capacity:
          break
        values += item["value"]
      if values > max_value:
        max_value = values
        best_weight = weights
        best_group = group
  
  return {
    'capacity': capacity,
    'items': list(best_group),
    'weight': best_weight,
    'value': max_value
  }

