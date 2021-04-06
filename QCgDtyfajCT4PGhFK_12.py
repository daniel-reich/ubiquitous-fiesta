
def prime_factorization(number):
  i=2
  k=[]
  while(number>1):
    if(number%i==0):
      number=int(number/i)
      k.append(i)
    else:
      i+=1
  return k

