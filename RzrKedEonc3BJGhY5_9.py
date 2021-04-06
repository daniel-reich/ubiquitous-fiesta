
def plant_trees(w, l, g):
  n_pl=2*w+2*(l-2)
  return n_pl//(g+1) if n_pl%(g+1)==0 else 0

