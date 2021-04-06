
def factorial(n):
  total = 1
  for i in range(1, n+1):
    total *= i
  return total
​
def kempner(n):
  i = 1
  while factorial(i) % n != 0:
    i += 1
  return i

