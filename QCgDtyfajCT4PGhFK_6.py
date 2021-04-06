
def prime_factorization(number):
  arr=[]
  c=2
  while number!=1:
    if number%c==0:
      arr.append(c)
      number=number/c
    else:
      c=c+1
  return arr

