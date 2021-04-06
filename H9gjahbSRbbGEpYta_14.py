
def multiply(n1, n2):
  ret = 0
  for i in range(abs(n2)):
    if n2>0:
      ret+=n1
    else:
      ret-=n1
  return ret

