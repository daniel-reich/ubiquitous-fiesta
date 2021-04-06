
def is_factorial(n):
  k, A = 1, 1
  while A<n:
    A*=k
    k+=1
    if A==n:
      return True
  return False

