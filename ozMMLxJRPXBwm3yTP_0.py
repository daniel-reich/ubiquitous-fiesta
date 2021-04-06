
def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)
​
def is_factorial(n):
  i = 0
  while factorial(i)<n:
    i +=1    
  return factorial(i) == n

