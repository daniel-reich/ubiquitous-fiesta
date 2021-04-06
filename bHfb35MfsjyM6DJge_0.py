
def route_diff(directions):
  ns = abs(directions.count('N')-directions.count('S'))
  ew = abs(directions.count('E')-directions.count('W'))
  return len(directions) - ns - ew

