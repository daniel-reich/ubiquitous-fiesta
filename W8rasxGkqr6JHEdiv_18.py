
from itertools import permutations as P, combinations_with_replacement as H
def countdown(operands, target):
  d=['+', '-', '*', '//']
  A=list(P(operands))
  B=list(H(d,len(operands)-1))
  C=[]
  for x in A:
    for y in B:
      k=''.join([str(j) for i in zip(x,y) for j in i]+[str(x[-1])])
      C.append((target-eval(k), k))
  D=sorted([x for x in C if x[0]>=0])   
  if D[0][0]==0:
    return D[0][1]
  else:
    quit()

