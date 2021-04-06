
def covered_integers(lst):
  return len(set(sum((list(range(a,b+1)) for a,b in lst),[])))

