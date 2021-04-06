
def product(lst):
  lst = sorted(set(lst), reverse = True)
  return lst[0] * lst[1] if len(lst) > 1 else lst[0]**2

