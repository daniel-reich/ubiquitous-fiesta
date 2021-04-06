
def prime_factorization(n):
  i, fact = 2, []
  while n>1:
    while n%i==0:
      fact+= [i]
      n//= i
    i+= 1
  return fact

