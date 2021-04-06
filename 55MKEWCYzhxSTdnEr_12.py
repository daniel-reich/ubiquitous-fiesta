
def gcd(a, b):
  k = res = 1 
  while k <= min(a,b) : 
    if a % k == 0 and b % k == 0 : res = k 
    k += 1
  return res

