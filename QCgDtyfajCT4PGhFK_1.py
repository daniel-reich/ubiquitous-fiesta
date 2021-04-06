
def prime_factorization(number):
  res = []
  i=2
  while i<=number:
    while number%i==0:
      res.append(i)
      number = number//i
    i+=1
  return res

