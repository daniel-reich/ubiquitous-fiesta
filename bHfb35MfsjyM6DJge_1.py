
def route_diff(directions):
  return len(directions)-(abs(directions.count('E')-directions.count('W'))+abs(directions.count('N')-directions.count('S')))

