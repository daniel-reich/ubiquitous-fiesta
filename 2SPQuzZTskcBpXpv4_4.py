
def euclidean(a, b):
  
  r = 1
  
  while (r != 0):
  
    if (a < b):
      Conduit1 = a
      Conduit2 = b
      a = Conduit2
      b = Conduit1
​
    r = a % b
​
    if (r == 0):
      return b
​
    else:
      Conduit3 = a
      Conduit4 = b
      Conduit5 = r
      a = Conduit4
      b = Conduit5

