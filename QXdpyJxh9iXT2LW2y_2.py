
def semiprimes(n):
  def prime(m):
    return not any([1 for j in range(2,int(m**(1/2))+1) if m%j==0])
  B=[i for i in range(2,n+1) if prime(i)==True]
  C=sorted(list(set([i*j for i in B for j in B if i*j<n])))
  D=list(filter(lambda x: True if not (x**(1/2)).is_integer() else False, C))
  return C,D

