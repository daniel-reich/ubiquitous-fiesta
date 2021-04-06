
def get_distance(a, b):
  xs = (abs(a['x'] - b['x']))**2
  ys = (abs(a['y'] - b['y']))**2
  return round((xs + ys)**(0.5), 3)

