
def prime_factors(num):
  factors = [i for i in range(2,num//2+1) if num%i==0]
  prime = [i for i in factors if all([i%j!=0 for j in range(2,i)])]
  res = []
  for i in prime:
    while num%i==0:
      res.append(i)
      num /= i
  return res

