
def parallel_resistance(lst):
  return round(sum([el ** -1 for el in lst]) ** -1 , 1)

