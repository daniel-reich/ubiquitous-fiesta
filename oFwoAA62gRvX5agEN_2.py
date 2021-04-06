
def knapsack(capacity, items):
  if (by_value(capacity, items)["value"] > by_value_per_weight(capacity, items)["value"]):
    return by_value(capacity, items)
  return by_value_per_weight(capacity, items)
  
def by_value(capacity, items):
  sorted_items = sorted(items, key=lambda k: k['value'])
  weight = 0  
  looted_items = []
  while (weight < capacity):
    if (len(sorted_items) == 0):
      break
    item = sorted_items.pop()
    if ((item["weight"] + weight) <= capacity):
      looted_items.append(item) 
      weight += item["weight"]
  final_items = [x for x in items if x in looted_items]
  value = sum(item["value"] for item in looted_items)
  return {
    "capacity": capacity,
    "items": final_items,
    "weight": weight,
    "value": value
  }
​
def by_value_per_weight(capacity, items):
  sorted_items = sorted(items, key=lambda k: k['value']/k["weight"])
  weight = 0  
  looted_items = []
  while (weight < capacity):
    if (len(sorted_items) == 0):
      break
    item = sorted_items.pop()
    if ((item["weight"] + weight) <= capacity):
      looted_items.append(item) 
      weight += item["weight"]
  final_items = [x for x in items if x in looted_items]
  value = sum(item["value"] for item in looted_items)
  return {
    "capacity": capacity,
    "items": final_items,
    "weight": weight,
    "value": value
  }

