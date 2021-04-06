
def covered_integers(lst):
  return len(set(y for x in lst for y in range(x[0], x[1] + 1)))

