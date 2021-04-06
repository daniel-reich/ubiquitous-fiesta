
def diamond_arrays(x):
  return [[i] * i for i in range(1, x)] + [[i] * i for i in range(x,0,-1)]

