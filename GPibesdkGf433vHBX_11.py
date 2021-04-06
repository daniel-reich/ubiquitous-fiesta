
def goldbach_conjecture(n):
  if n%2==1:
    return []
  for i in range(2,n):
    for j in reversed(range(i,n)):
      if is_prime(i) and is_prime(j) and i+j==n:
        return [i,j]
​
def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

