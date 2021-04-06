
def is_parallelogram(lst):
  xs = sorted([x[0] for x in lst])
  ys = sorted([y[1] for y in lst])
  is_x = abs(xs[1]-xs[0]) == abs(xs[3]-xs[2])
  is_y = abs(ys[1]-ys[0]) == abs(ys[3]-ys[2])
  return all([is_x, is_y])

