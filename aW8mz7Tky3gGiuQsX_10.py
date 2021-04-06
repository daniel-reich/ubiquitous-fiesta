
def is_powerful(n):
  lst = [k for k in range(2,n) if prime(k) and n%k == 0]
  for elem in lst:
    if n%(elem**2): return False
  return True
​
def prime(num):
  if num < 2: return False
  for i in range(2,num):
    if num%i == 0: return False
  return True

