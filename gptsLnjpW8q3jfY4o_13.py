
import re
def pascal_row(n):
  row=[0]*(n+1)
  row[0] = row[n] = 1
  for i in range(0, n>>1):
    x = row[ i ] * (n - i) // (i + 1)
    row[ i + 1 ]= row[ n - 1 - i ] = x
  return row
def Formula(n):
  if n!=-1:
    m=abs(n)
    A=['a^{}b^{}'.format(x,y) for x, y in zip(range(m, -1, -1), range(m+1))]
    for i in range(len(A)):
      A[i]=re.sub(r'[ab]\^0', '', A[i])
      A[i]=re.sub(r'\^1(?=[b])','', A[i])
      A[i]=re.sub(r'\^1$','', A[i])
    res=[str(pascal_row(m)[i])+A[i] for i in range(len(A))]
    res[0]=res[0][1:]
    res[-1]=res[-1][1:]
    t='+'.join(res)
    if n>0:
      return t
    elif n<0:
      return '1/({})'.format(t)
    else:
      return '1'
  else:
    return "1/(a+b)"

