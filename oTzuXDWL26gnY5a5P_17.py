
def prime(n):
  if n < 2: return False
  for i in range(2,n):
    if n%i==0: return False
  return True
def prime_numbers(num):
  return sum(prime(i) for i in range(num))

