
def get_distance(a, b):
  import math
  side_1 = a['y'] - b['y']
  side_2 = a['x'] - b['x']
  return round(math.sqrt(side_1 ** 2 + side_2 ** 2), 3)

