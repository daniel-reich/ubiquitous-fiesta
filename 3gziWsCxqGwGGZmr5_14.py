
def fat_prime(a, b):
  if b < a:
    c = a
    a = b
    b = c
  
  for i in range(b,a-1,-1):
    isPrime = True
    for j in range(2,int(i**.5)+1):
      if i % j == 0:
        isPrime = False
    if isPrime:
      return i

