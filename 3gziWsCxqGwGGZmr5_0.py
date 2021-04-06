
def fat_prime(a, b):
  n = max(a,b)
  while n > 0:
    if n % 10 in [1,3,7,9]:
      if any(not n%i for i in range(2,int(n**0.5)+1)):
        pass
      else:
        return n
    n -= 1

