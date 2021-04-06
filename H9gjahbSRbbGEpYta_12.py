
def multiply(n1, n2):
  
  Total = 0
  
  Added = 0
  Required = abs(n2)
  
  while (Added < Required):
    Total += n1
    Added += 1
    
  if (n2 < 0):
    return Total * -1
  else:
    return Total

