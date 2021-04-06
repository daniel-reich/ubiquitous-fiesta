
def showdown(p1, p2):
  if (p1.find('B') > p2.find('B')):
    return 'p2'
  elif p1.find('B') == p2.find('B'):
    return 'tie'
  return 'p1'

