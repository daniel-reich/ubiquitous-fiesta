
from collections import Counter as C
def frequency_sort(s):
  A=[x*C(s)[x] for x in C(s)]
  A=sorted(A, key=lambda x: (-len(x), x[0]))
  return ''.join(A)

