
def diamond_arrays(x):
  a= [[y]*y for y in range(1,x+1)]
  return a+a[:-1][::-1]

