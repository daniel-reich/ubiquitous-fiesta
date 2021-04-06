
def plant_trees(w, l, g):
  p = 2*w + 2*(w-2)
  if p%(g+1)==0:
    return p/(g+1)
  return 0

