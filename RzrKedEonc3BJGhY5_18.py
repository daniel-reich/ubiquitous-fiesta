
def plant_trees(w, l, g):
  remainder = (w + (w - 1) * 2 + 1) % (g + 1)
  if w != l or (g > w and g > l) or remainder > 0:
    return 0
  else:
    return (w + (w - 1) * 2 + (w - 2)) // (g + 1)

