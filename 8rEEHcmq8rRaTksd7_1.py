
def lines_are_parallel(l1, l2):
  x0, y0, z0 = l1
  x1, y1, z1 = l2
  try: return x0//x1 == y0//y1
  except ZeroDivisionError: return x0 == x1 or y0 == y1

