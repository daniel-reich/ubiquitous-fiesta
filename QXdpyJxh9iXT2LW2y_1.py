
from itertools import*
def semiprimes(n):
  p=[i for i in range(2,int(n/2)+1)if all(i%x for x in range(2,int(i**0.5+1)))]
  q=sorted(x*y for x,y in combinations(p,2)if x*y<n)
  return sorted(q+[x*x for x in p if x*x<n]),q

