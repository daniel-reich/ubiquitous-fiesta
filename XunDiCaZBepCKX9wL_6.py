
from itertools import combinations as C
def secret_word(s, l):
  A=[s[i:i+3] for i in range(len(s)-2)]
  B=[sum([ord(x)-ord('a')+1 for x in y]) for y in A]
  B=[(x,i) for i, x in enumerate(B)]
  F=[x for x in C(B,l) if all(x[i][0]-x[i+1][0]==x[0][0]-x[1][0] for i in range(len(x)-1))]
  D=[F[0][i][1] for i in range(l)]
  E=[A[i][1] for i in D]
  return ''.join(E) if l<8 else quit()

