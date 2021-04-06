
def product(lst):
  lst = sorted(set(lst))[-2:]
  return lst[0] * lst[-1]

