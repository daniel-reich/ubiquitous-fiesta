
def i_sqrt(n):
  stepcounter = 0
  if n < 1:
    return "invalid"
  while not n < 2:
    n = n**0.5
    stepcounter += 1
  
  return stepcounter

