
def parallel_resistance(lst):
  res = 0
  for R in lst:
    res += 1/R
  res = 1/res
  
  return round(res, 1)

