
def factorial(n):
  aux = n
  n = n-1
  if(n > 0):
    aux = aux * factorial (n)
  else:
    aux = 1;
  return aux

