
def multiply(n1,n2):
  if n1 == 0 or n2 == 0:
    return 0
  prod = 0 
  
  if n2 > 0:
    for i in range(1,n2+1):
      prod += n1
    return prod
  if n2 < 0:
    for i in range(n2,0):
      prod -= n1
  return prod

