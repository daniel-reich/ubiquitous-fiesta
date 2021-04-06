
def prime_factorize(num):
  p=[]
  for d in range(2,num+1):
    while num%d==0:
      p.append(d)
      num//=d
  return p

