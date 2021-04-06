
def factors(n):
​
  f,i = [],0
  
  for i in range(2,n):
    while not n%i:
      n/=i
      f.append(i)
​
    i += 1
​
  return list(set(f))
​
def is_prime(l):
​
  for e in l:
    for i in range(2,n):
      if not e%i:
        l.pop(e)
​
  return l
​
def is_powerful(n):
  
  fs = factors(n)
  
  for i in fs:
    if n%(i**2):
      return False
​
  return True

