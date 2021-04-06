
def plant_trees(w, l, g):
  #works for square shape
  dots = (w - 1) * 4
  result = dots / (g + 1)
  return result if result.is_integer() else 0
  
  #for any shape
  #dots = 2 * w + 2 * l - 4
  #result = dots / (g + 1)
  #return result if result.is_integer() else 0

