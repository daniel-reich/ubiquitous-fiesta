
import re
from itertools import permutations as P
def greater_permutation(expr, nums):
  expr=re.sub('[abc]', '{}', expr)
  A=[expr.format(*x) for x in P(nums)]
  e=max(A, key=eval)
  k=int(eval(e)) if eval(e)%1==0 else round(eval(e),2)
  return '{} = {}'.format(e, k)

