
def kempner(n):
  for i in range(1, n+1):
    if factorial(i) % n == 0:
      return i
​
def factorial(num):
  f = 1
  if num == 0:
     return 1
  for i in range(1,num + 1):
    f *= i
  return f

