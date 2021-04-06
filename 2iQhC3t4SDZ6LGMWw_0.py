
def on_rectangle_bounds(pts):
  xs = [min(p[0] for p in pts),max(p[0] for p in pts)]
  ys = [min(p[1] for p in pts),max(p[1] for p in pts)]
  return all(p[0] in xs or p[1] in ys for p in pts)

