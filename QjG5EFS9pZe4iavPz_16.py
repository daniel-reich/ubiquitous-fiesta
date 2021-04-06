
def fib(n):
  if n == 1 or n ==2:
    a = 1
    return a
  elif n == 0:
    a = 0
    return a
  d = [2,3]
  a = 2
  b= 3
  for i in range(n):
    a = a +b 
    d.append(a)
    b = b + a
    d.append(b)
  print(d[n-3])
  return d[n-3]

