
def showdown(p1, p2):
  t1 = p1.index('Bang!')
  t2 = p2.index('Bang!')
  return 'p1' if t1 < t2 else 'p2' if t1 > t2 else 'tie'

