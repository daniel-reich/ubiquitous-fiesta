
def covered_integers(lst):
  return len(set(j for i in lst for j in range(i[0], i[1] + 1)))

