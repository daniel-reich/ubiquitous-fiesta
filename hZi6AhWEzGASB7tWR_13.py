
def check(lst):
  if all(x<y for x, y in zip(lst, lst[1:])):
    return "increasing"
  elif all(x>y for x, y in zip(lst, lst[1:])):
    return "decreasing"
  else:
    return "neither"

