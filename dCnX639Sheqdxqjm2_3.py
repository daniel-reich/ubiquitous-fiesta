
def parallel_resistance(lst):
  runningsum = 0
  for r in lst:
    runningsum += (1/r)
  return round(1/runningsum,1)

