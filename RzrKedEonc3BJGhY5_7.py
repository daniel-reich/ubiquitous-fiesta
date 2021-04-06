
def plant_trees(w, l, g):
  trees = 2 * (w + l - 2) / (g + 1)
  return 0 if trees % 1 else trees

