
def fat_prime(a, b):
  s, e = min(a,b), max(a,b)
  return max(i for i in range(s,e+1) if all(i%j for j in range(2,int(i**0.5)+1)))

