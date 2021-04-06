
def prime_divisors(num):
  if prime(num):
    return [num]
  lst = [i for i in range(2,num//2) if num%i==0]
  return [i for i in lst if prime(i)]
  
def prime(n):
  for i in range(2,n//2+1):
    if n%i==0:
      return False
  return n>1

