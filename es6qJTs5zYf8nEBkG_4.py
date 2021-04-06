
def is_rectangle(coords):
  if len(set(coords)) != 4:
    return False
    
  coords = [eval(i) for i in coords]
  (x1, y1), (x2, y2), (x3, y3), (x4, y4) = sorted(coords, key=lambda x: (x[0], x[1]))
  return x1 == x2 and x3 == x4 and y1 == y3 and y2 == y4

