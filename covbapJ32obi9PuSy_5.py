
def diamond_arrays(x):
  return [[i] * i for i in range(1, x + 1)] + [[j] * j for j in range(x - 1, 0, -1)]

