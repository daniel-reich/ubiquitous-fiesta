
def covered_integers(lst):
  return len(set(r for i in lst for r in range(i[0], i[1]+1)))

