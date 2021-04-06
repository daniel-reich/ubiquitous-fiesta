
def diamond_arrays(x):
  lst = [[n]*n for n in range(1, x+1)]
  return lst + lst[:-1][::-1]

