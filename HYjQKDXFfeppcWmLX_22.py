
def is_curzon(num):
  A=2**num+1
  B=num*2+1
  if A%B==0:
    return True
  else:
    return False

