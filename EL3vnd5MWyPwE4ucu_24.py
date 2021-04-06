
def fibonacci(n):
  a,b=0,1
  for x in range(n-1):
    a,b = b,a+b
  return str(b)

