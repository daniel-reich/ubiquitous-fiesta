
def showdown(p1, p2):
  a=p1.index("B")
  b=p2.index("B")
  if a<b:
    return 'p1'
  elif a==b:
    return "tie"
  else :
    return 'p2'

