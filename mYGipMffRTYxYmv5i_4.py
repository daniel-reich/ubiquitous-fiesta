
from itertools import permutations as P
def simple_equation(a, b, c):
  A=[x for x in P((a,b,c))]
  for x in A:
    for t in ['+', '-', '*', '//']:
      if eval('{}{}{}'.format(x[0],t,x[1]))==x[2]:
        return '{}{}{}={}'.format(x[0],t,x[1],x[2]).replace('//','/')
  return ''

