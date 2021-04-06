
def multiply(n1, n2):
  i=0
  n=0
  while i<abs(n2):
    n+=n1
    i+=1
  if n2>0:
    return n
  else:
    return -n

