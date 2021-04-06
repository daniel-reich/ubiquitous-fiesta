
def route_diff(directions):
  NS = min(directions.count('N'),directions.count('S'))*2
  EW = min(directions.count('E'),directions.count('W'))*2
  return NS+EW

