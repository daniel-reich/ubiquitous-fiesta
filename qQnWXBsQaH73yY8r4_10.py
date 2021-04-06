
def kempner(n):
  return len([i for i in range(1,n+1) if factorial(i)%n>0 or n == 1])
  
def factorial(n):
  ans = 1
  for i in range(1,n):
    ans *= i
  return ans

