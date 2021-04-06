
from itertools import permutations
import re
​
def greater_permutation(expr, nums):
  expr = re.sub('[abc]', '{}', expr)
  best = max((i for i in permutations(nums)), key=lambda x: eval(expr.format(*x)))
  expr = expr.format(*best)
  res = round(eval(expr), 2)
  return '{} = {}'.format(expr, res if res%1 else int(res))

