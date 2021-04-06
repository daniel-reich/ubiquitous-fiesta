
def fat_prime(a, b):
  for i in range(max(a,b),min(a,b),-1):
    if all([i%j for j in range(2,i)]):return i

