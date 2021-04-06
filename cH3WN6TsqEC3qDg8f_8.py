
def rectangle_in_circle(w, h, r):
  w = w / 2
  h = h / 2
  return r >= (w**2 + h**2)**.5

