
def multiply(n1, n2):
  p = True
  if n1 < 0 and n2 < 0:
    n1 = abs(n1)
    n2 = abs(n2)
  elif n1 < 0 or n2 < 0:
    p = False
    n1 = abs(n1)
    n2 = abs(n2)
  
  myans = n1
  while n2 > 1:
    myans += n1
    n2 -= 1
  
  if p:
    return myans
  else:
    return int('-' + str(myans))

