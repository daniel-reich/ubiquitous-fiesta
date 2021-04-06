
def is_prime(n):
  return n>1 and all(n%i for i in range(2, int(n**.5)+1))
def sum_prime(lst):
  P=[x for x in range(2, max(lst)+1) if is_prime(x)]
  A=[]
  for x in P:
    B=[]
    for y in lst:
      if y%x==0:
        B.append(y)
    if B:
      A.append(str((x,sum(B))))
  return ''.join(A).replace(',', '')

