
def showdown(p1, p2):
  v = p1.find('B') - p2.find('B')
  return 'p1' if v < 0 else 'p2' if v > 0 else 'tie'

