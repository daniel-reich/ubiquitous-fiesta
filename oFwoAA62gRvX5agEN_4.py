
def knapsack(capacity, items):
  dpCache = {(0,-1):(0, [])}
  def dp_knapsack(cap, itmIdx):
    if (cap, itmIdx) in dpCache:
      return dpCache[(cap, itmIdx)]
    elif cap < 0 or itmIdx < 0:
      return None
    
    options = [dp_knapsack(cap, itmIdx - 1), 
              dp_knapsack(cap - 1, itmIdx)]   
    temp = dp_knapsack(cap - items[itmIdx]['weight'], itmIdx -1)
    if temp is not None:
      options.append((temp[0] + items[itmIdx]['value'], temp[1][:] + [itmIdx]))
    options = filter(lambda x: x is not None, options)
    
    choice = max(options, key=lambda x:x[0])
    dpCache[(cap, itmIdx)] = choice
    return choice
    
  optimal = dp_knapsack(capacity, len(items) - 1)
  out = {"capacity":capacity, "items":[], "weight":0, "value":optimal[0]}
  for idx in optimal[1]:
    out["items"].append(items[idx])
    out["weight"] += items[idx]["weight"]
  print(dpCache)
  return out

