
def combinations(*args):
  ans = 1
  for arg in args:
    if arg > 0:
      ans *= arg
  return ans

