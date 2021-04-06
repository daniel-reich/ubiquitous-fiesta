
def overlapping_rectangles(rect1, rect2):
  l, b, w, h = zip(rect1, rect2)
  r = [l[i] + w[i] for i in [0, 1]]
  t = [b[i] + h[i] for i in [0, 1]]
  x_o = min(r) - max(l)
  y_o = min(t) - max(b)
  return 0 if x_o < 0 or y_o < 0 else x_o * y_o

