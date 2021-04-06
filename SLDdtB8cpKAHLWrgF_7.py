
from itertools import permutations
def greater_permutation(expr, nums):
  max_res = - float('inf')
  for p in permutations(nums):
    expr_num = expr.replace('a',str(p[0])).replace('b',str(p[1])).replace('c',str(p[2]))
    res = eval(expr_num)
    if res > max_res:
      if isinstance(res,float):
        res = int(res) if res.is_integer() else round(res,2)
      best = expr_num + ' = {}'.format(res)
      max_res = res
  return best

