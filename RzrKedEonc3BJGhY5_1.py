
def plant_trees(w, l, g):
  trees = (w+l-2)*2/(g+1)
  return trees if not trees % 1 else 0

