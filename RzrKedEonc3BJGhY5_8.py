
def plant_trees(w, l, g):
  spaces = (w * l) - ((w - 2)**2)
  if spaces % (g + 1) != 0:
    return 0
  else:
    return spaces // (g + 1)

