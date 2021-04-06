
def fibo(n):
  a = 1
  b = 1
  c = 0
  for i in range(1, n):
    a = b + c
    c = b
    b = a
​
  return a

