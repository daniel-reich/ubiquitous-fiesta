
def prime_factorize(num):
  y = []
  for n in range(2,num+1):
    while num%n==0:
      y.append(n)
      num = num/n
  return y

