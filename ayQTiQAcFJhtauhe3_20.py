
def even_or_odd(lst):
  if sum(lst) % 2 == 0:
    result = "even"
  elif sum(lst) % 2 == 1:
    result = "odd"
  return result

