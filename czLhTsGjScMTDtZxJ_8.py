
def primorial(n):
  count = 0
  fin = 1
  cur = 2
  while count<n:
    if is_prime(cur):
      count+=1
      fin*=cur
    cur+=1
  return fin
​
def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

