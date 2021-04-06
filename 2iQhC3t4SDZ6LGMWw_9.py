
def on_rectangle_bounds(points):
  b, t = min(points,key=lambda x: x[1])[1], max(points,key=lambda x: x[1])[1]
  l, r = min(points,key=lambda x: x[0])[0], max(points,key=lambda x: x[0])[0]
​
  for p in points:
    if p[0] in [l,r]:
      if not b <= p[1] <= t:
        return False
    elif p[1] in [b,t]:
      if not l <= p[0] <= r:
        return False
    else:
      return False
  return True

