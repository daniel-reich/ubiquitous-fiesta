
def knapsack(capacity, items):
​
  # check all items based on profitability index
  capacity2 = capacity
  for i in range(len(items)):
    items[i]["num"] = i
    items[i]["profitability"] = items[i]["value"] / items[i]["weight"]
  ca, it, we, va = capacity, [], 0, 0
  items.sort(key = lambda x: x["profitability"], reverse = True)
  for i in items:
    if i["weight"] <= capacity:
      capacity = capacity - i["weight"]
      it.append(i)
      we = we + i["weight"]
      va = va + i["value"]
  items.sort(key = lambda x: x["num"])
  it.sort(key = lambda x: x["num"])
  for i in items:
    del i["num"]
    del i["profitability"]
        
  # check all items based on highest value
  for i in range(len(items)):
    items[i]["num"] = i
    items[i]["profitability"] = items[i]["value"] / items[i]["weight"]
  ca2, it2, we2, va2 = capacity2, [], 0, 0
  items.sort(key = lambda x: x["value"], reverse = True)
  for i in items:
    if i["weight"] <= capacity2:
      capacity2 = capacity2 - i["weight"]
      it2.append(i)
      we2 = we2 + i["weight"]
      va2 = va2 + i["value"]
  items.sort(key = lambda x: x["num"])
  it2.sort(key = lambda x: x["num"])
  for i in items:
    del i["num"]
    del i["profitability"]
  
  if va > va2:
    return {
    'capacity': ca,
    'items': it,
    'weight': we,
    'value': va
    }
    
  return {
  'capacity': ca2,
  'items': it2,
  'weight': we2,
  'value': va2
  }

