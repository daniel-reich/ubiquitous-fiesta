
def flatten(lst):
  return sum((flatten(l) for l in lst),[]) if type(lst)==list else [lst]

