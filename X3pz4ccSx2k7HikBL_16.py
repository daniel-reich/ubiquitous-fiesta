
def showdown(p1, p2):
  p1B = p1.find("B")
  p2B = p2.find("B")
  if p1B < p2B:
    return "p1"
  elif p1B > p2B:
    return "p2"
  else: 
    return "tie"

