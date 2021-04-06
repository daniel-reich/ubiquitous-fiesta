
def showdown(p1, p2):
  shot1, shot2 = p1.index('B'), p2.index('B')
  return 'p1' if shot1 < shot2 else 'p2' if shot2 < shot1 else 'tie'

