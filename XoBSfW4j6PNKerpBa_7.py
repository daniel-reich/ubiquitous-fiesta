
def complete_factorization(num):
  res=[]
  for n in [i for i in range(2,num+1) if not num%i]:
    while not num%n:
      num=num//n
      res+=[n]
  return res

