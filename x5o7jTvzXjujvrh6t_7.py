
def i_sqrt(n):
  if n >= 0:
    i=0
    while n >= 2:
      n = n**(1/2)
      i +=1
    return i
  else: 
    return "invalid"

