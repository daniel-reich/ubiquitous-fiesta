
def plant_trees(w, l, g):
  points = (w * 2 + l * 2 - 4)  / (g + 1)
  
  if points.is_integer():
    return points
  return 0

