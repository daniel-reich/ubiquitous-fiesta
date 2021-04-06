
def fib(n):
  b =1
  a = 1
  d = 0
  if n==1 or n==2 :
    return 1
  if n==0 :
    return 0
  else :
    for i in range(3 , n+1):
      d = a
      a= b
      b = b + d
    return b

