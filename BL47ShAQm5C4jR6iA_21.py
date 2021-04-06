
def third_most_expensive(dct):
  
  if len(list(dct.keys())) < 3:
    return False
  
  goal_price = sorted(list(dct.values()))[-3]
  
  for k in dct.keys():
    if dct[k] == goal_price:
      return k

