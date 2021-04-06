
def showdown(p1, p2):
  x = p1.index('B')
  y = p2.index('B')
  if x == y:
    return 'tie'
  elif x < y:
    return 'p1'
  else:
    return 'p2'

