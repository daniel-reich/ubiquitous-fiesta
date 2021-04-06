
def showdown(p1, p2):
  if len(p1.rstrip()) == len(p2.rstrip()) : 
    return "tie"
  elif len(p1.rstrip()) > len(p2.rstrip()) :
    return "p2"
  else : 
    return "p1"

