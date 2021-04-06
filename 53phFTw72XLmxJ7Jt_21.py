
def marathon_distance(d):
  distance = 0
  for miles in d:
    if miles < 0:
      distance -= miles
    if miles > 0:
      distance += miles
  return distance == 25

