
def showdown(p1, p2):
  play1 = p1.find("Bang")
  play2 = p2.find("Bang")
  
  if play1 == play2:
    return "tie"
  elif play1 < play2:
    return "p1"
  else:
    return "p2"

