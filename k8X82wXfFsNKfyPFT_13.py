
def clone(lst):
  res = []
  for x in lst:
    res.append(x)
  res.append(lst) 
  return res

