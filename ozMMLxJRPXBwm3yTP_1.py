
def is_factorial(n):
  i,f = 1,1
  while f < n:
    i+=1
    f*= i
  return n == f

