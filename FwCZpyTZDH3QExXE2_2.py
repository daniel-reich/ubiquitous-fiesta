
def amount_fib(n):
  if n<2: return n
  
  a = 1
  b = 1
  cnt = 2
  
  while b<n:
    a,b = b,a+b
    cnt+=1
  
  return cnt

