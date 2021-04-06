
def prime_factorize(num):
  x = []
  for i in range(2,num+1):
    while num%i==0: x += [i]; num /= i
  return x

