
def rectangle_in_circle(w, h, r):
  sc = 3.14 * r ** 2
  sr = w * h
  ls = (w ** 2 + h ** 2) ** .5
  return True if sr < sc and ls <= r * 2 else False

