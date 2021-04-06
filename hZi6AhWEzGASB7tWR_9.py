
def check(lst):
  for i in lst:
    if lst.count(i) > 1:
      return "neither"
  if lst == sorted(lst):
    return "increasing"
  elif lst == sorted(lst , reverse = True):
    return "decreasing"
  else:
    return "neither"

