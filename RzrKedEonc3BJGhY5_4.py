
def plant_trees(w, l, g):
  if w != l:
    return (0)
  perimiter = (w * 4) - 4
  print("Perimiter: %s" % perimiter)
  lengths = perimiter/(g+1)
  print("Lengths for gap of %s: %s" % (g, lengths))
  if perimiter % lengths != 0:
    return (0)
  else:
    return lengths

