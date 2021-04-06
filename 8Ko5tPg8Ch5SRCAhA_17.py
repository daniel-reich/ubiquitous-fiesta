
def fibonacci(num):
  x,y=0,1
  n=1
  while n<=num:
    x,y=y,x+y
    n+=1
  return y

