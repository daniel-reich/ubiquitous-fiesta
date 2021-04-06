
def plant_trees(w, l, g):
  q,r=divmod(2*(w-1)+2*(l-1),g+1)
  return q if r==0 else 0

