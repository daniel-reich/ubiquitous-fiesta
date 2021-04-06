
def is_curzon(num):
  first = 2**num + 1
  second = 2*num + 1
  return True if first%second == 0 else False

