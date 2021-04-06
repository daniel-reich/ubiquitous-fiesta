
def points_in_circle(points, centerX, centerY, radius):
  radius=float(radius)
  coords = []
  total=0
  for point in points:
    for v in point.values():
      coords.append(v)
  for i in range (0, len(coords), 2):
    x1=coords[i]
    y1=coords[i+1]
    x2=centerX
    y2=centerY
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    #print (d, radius, total)
    if d<radius:
      total+=1
  return total

