
def prime(n):
  if n<2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n%i==0:
      return False
  return True
​
def goldbach_conjecture(n):
  if n < 2 or n %2 ==1:
    return []
  for i in range(2, n):
    if prime(i) and prime(n-i):
      return [i, n-i]

