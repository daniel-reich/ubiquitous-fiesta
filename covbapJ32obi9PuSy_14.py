
def diamond_arrays(x):
  lst = [[i]*i for i in range(1, x+1)]
  return lst + lst[-2::-1]

