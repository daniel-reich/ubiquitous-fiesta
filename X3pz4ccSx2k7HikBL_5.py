
def showdown(p1, p2):
  p1 = len(p1.split('B')[0])
  p2 = len(p2.split('B')[0])
  return 'tie' if p1 == p2 else 'p1' if p1 < p2 else 'p2'

