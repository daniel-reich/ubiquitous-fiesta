
from itertools import permutations as P
import random
def numbers():
  A=list(P(range(1, 6)))
  return int(''.join([str(k) for k in A[random.randint(0,len(A)-1)]]))

