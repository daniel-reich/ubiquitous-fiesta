
def diamond_arrays(x):
  A=[[i]*i for i in range(1, x+1)]
  return A+A[:-1][::-1]

