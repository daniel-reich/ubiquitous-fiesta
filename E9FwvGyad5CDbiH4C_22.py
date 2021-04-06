
def block(lst): 
  rot = list(zip(*lst[::1]))
  blo = len(lst)*len(rot) 
  for x in rot:   
    blo -= (x.index(2) + 1) if 2 in x else len(lst)
  return blo

