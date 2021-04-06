
def multiply(n1, n2):
  a=0
  neg=False
  if (n1<0 or n2<0) and not (n1<0 and n2<0):
    neg=True
  n1=abs(n1)
  n2=abs(n2)
  for i in range(n2):
    a+=n1
  
  return a if not neg else a-a-a

