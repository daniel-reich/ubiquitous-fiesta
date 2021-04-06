
def showdown(p1, p2):
  if str.find(p1, 'B') < str.find(p2, 'B'):
    return 'p1'
  elif str.find(p1, 'B') == str.find(p2, 'B'):
    return 'tie'
  return 'p2'

