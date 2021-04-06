
def even_or_odd(lst):
  if len(lst) == 0:
    return "even"
  if sum(lst) % 2 == 0:
    return "even"
  else:
    return "odd"

