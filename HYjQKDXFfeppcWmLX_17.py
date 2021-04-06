
def is_curzon(num):
  none=2**num+1
  ntwo=2*num+1
  if none%ntwo==0:
    return True
  else:
    return False
is_curzon(5)

