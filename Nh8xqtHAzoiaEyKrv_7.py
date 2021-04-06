
import re
def correct_sentences(s):
  s=s.lstrip().rstrip()
  p=r'\s+(?=[A-Z])'
  H=[x for x in s.split() if x!=' ']
  k=' '.join(H)
  A=re.split(p,k)
  A[0]=A[0].capitalize()
  for i in range(len(A)):
    A[i]+='.'
  return ' '.join(A)

