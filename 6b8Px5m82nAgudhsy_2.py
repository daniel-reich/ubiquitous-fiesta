
import itertools as it
def next_number(n):
  if n<10:return n
  s=str(n)
  l=sorted(set(it.permutations(s,len(s))))
  p=l.index(tuple(s))
  return int(''.join(l[p+1]))if p!=len(l)-1else n

