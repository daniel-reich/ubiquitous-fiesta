
def swap_dict(d):
  nd = {}
​
  for k, v in d.items():
    if v not in nd.keys():
      nd.update({v: [k]})
    else:
      nd[v].append(k)   
​
  return nd

