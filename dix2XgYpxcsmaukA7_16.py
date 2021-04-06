
def is_prime(n):
  return n>1 and all(n%i for i in range(2, int(n**0.5)+1))
def express_factors(n):
  A=[x for x in range(2, n+1) if n%x==0 and is_prime(x)]
  B=[]
  for x in A:
    i=0
    while n%x**i==0:
      i+=1
    B.append((x,i-1))
  C=[str(x[0])+'^{}'.format(x[1])*(x[1]!=1)  for x in B]
  return ' x '.join(C)

