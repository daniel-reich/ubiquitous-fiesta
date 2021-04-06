
def is_curzon(num):
  if (1+2**num)%(1+2*num) == 0:
    return True
  else:
    return False

