
def showdown(p1, p2):
  if p1.index("B") == p2.index("B"):
    return "tie"
  elif p1.index("B") > p2.index("B"):
    return "p2"
  else:
    return "p1"

