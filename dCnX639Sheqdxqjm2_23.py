
def parallel_resistance(lst):
  res = 0
  for el in lst:
    res += 1 / el
  return round(pow(res, -1),1)

