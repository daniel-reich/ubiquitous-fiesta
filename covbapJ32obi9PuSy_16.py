
def diamond_arrays(x):
  left = [[i]*i for i in range(1,x+1)]
  right = list(reversed(left[:-1]));
  return left + right;

