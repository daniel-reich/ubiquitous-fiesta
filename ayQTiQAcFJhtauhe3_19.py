
def even_or_odd(lst):
  if sum(lst) == 0:
    return 'even'
  elif (sum(lst) % 2) == 0:
    return 'even'
  else:
    return 'odd'

