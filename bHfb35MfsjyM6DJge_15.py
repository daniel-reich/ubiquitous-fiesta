
def route_diff(directions):
  l = directions.copy()
  while 'N' in l and 'S' in l:
    l.remove('N')
    l.remove('S')
  while 'E' in l and 'W' in l:
    l.remove('E')
    l.remove('W')
  return len(directions) - len(l)

