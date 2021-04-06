
def parallel_resistance(lst):
  ans = 0
  for x in lst: ans += 1/x 
  return round(1/ans, 1)

