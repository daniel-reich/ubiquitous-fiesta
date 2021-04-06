
def is_factorial(n):
  i=1
  while(n>1):
    if(n%i==0):
      n=int(n/i)
      i+=1
    else:
      return False
  return True

