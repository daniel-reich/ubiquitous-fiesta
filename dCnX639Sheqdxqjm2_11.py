
def parallel_resistance(lst):
  return round(1/sum(1/e for e in lst), 1)

