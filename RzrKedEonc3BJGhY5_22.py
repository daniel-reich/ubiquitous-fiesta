
def plant_trees(w, l, g):
  trees = (w*2+(l-2)*2)%(1+g)
  if trees == 0:
    return (w*2+(l-2)*2)/(1+g)
  else:
    return 0

