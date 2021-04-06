
def diamond_arrays(x):
  return [[n]*n for n in range(1,x+1)]+[[n]*n for n in range(x-1,0,-1)]

