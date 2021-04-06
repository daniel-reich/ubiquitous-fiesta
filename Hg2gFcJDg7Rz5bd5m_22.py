
def intersection(dict1, dict2):
  d3 = {} 
  d4 = {} 
  for k, v in dict1.items():
    if k in dict2:
      d3[k] = v
​
  for k, v in dict2.items():
    if k in dict1:
      d4[k] = v
​
  return [d3, d4]

