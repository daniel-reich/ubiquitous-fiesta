
import re
def group_seats(lst, n):
  A=[''.join([str(x[i]) for i in range(len(x))]) for x in lst]
  s=' '.join(A)
  p='0'+'{'+'{},'.format(n)+'}'
  B=re.findall(p, s)
  c1=B.count('0'*n)
  C=[x for x in B if len(x)>n]
  c2=sum([len(x)-n+1 for x in C])
  return c1+c2

