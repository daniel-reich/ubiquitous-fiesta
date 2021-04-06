
def gcd(a, b):
  ret = []
  for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
      ret.append(i)
  
  return  max(ret)

