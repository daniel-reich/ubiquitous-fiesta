
def plant_trees(w, l, g):
  x = ((l-1)*2 +(w-1)*2)
  if x%(g+1) == 0:
    return  int(x/(g+1))
  else:
    return 0

