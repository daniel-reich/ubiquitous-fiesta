
def is_prime(x):
  toggle=1
  if x==1 or x==4:
    return False
  for i in range(2,x//2):
    if x%i==0:  
      toggle=0
  return bool(toggle)
​
def sum_primes(lst):
  return sum([i for i in lst if is_prime(i)]) if len(lst)>0 else None

