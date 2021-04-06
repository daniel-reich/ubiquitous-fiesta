
def isPrime(val):
  for i in range(2, val):
    if val % i == 0: return False
    else: continue
  return True
​
def next_prime(val):
  for i in range(val, val+100):
    if isPrime(i): return i
    else: continue
  return False

