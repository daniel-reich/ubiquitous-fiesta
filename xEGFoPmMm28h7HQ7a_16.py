
def letter_combinations(digits):
  import itertools
  c=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
  n=[]
  for i in digits: n.append(int(i)-2)
  r0=[]
  for i in n:r0.append(c[i])
  r1=[]
  r1=list(itertools.product(*r0))
  r2=[]
  for i in r1: r2.append("".join(i))
  return r2

