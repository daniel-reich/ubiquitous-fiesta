
def parallel_resistance(lst):
  sum = 0
  for r in lst:
    sum = sum + (1/r)
  return round(sum ** -1, 1)

