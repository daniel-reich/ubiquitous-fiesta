
def complete_factorization(num):
  fact = []
  for r in range(2,num+1):
    while num%r==0:
      fact+= [r]
      num//=r
  return fact

