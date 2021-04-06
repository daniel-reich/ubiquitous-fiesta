
def direction(lst):
  return [x.replace("e","w").replace("a","e").replace("E","W").replace("A","E") for x in lst]

