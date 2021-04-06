
def showdown(p1, p2):
  x=p1.index("B")
  y=p2.index("B")
  return "p1" if y>x else "p2" if x>y else "tie"

