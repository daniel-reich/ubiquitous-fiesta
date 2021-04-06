
def on_rectangle_bounds(points):
  x0 = min(p[0] for p in points)
  x1 = max(p[0] for p in points)
  y0 = min(p[1] for p in points)
  y1 = max(p[1] for p in points)
  return all( ((x == x0 or x == x1) and (y >= y0 and y <= y1)) or \
              ((y == y0 or y == y1) and (x >= x0 and x <= x1)) \
              for x, y in points )

