
def plant_trees(w, l, g):
  
  if (l==1 or w==1): holes = l*w
  elif (l>1 and w>1): holes = 2*l + 2*w - 4
  else: return 0
  
  if (holes % (g+1) != 0): return 0
  else: return holes // (g+1)

