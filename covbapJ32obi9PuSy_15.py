
def diamond_arrays(x):
  res = [[i]*i for i in range(1, x+1)]
  return res + res[:-1][::-1]

