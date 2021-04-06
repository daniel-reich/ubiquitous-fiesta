
def points_in_circle(pts, cX, cY, r):
  L2 = lambda a, b: ((a[0] - b[0])**2 + (a[1] - b[1])**2)**.5
  return sum(1 for p in pts if L2((p['x'], p['y']), (cX, cY)) < r)

