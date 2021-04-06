
def covered_integers(lst):
  return len({i for l, u in lst for i in range(l, u+1)})

