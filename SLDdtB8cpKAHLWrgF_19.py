
from itertools import permutations 
def greater_permutation(expr, nums):
  expr = expr.replace("a", "{}").replace("b", "{}").replace("c", "{}")
  results = []
  for i in permutations(nums):
    x = eval(expr.format(i[0], i[1], i[2]))
    if x %1 == 0: x = round(x)
    else: x = round(x,2)
    results.append([x, expr.format(i[0], i[1], i[2]) + " = " + str(x)])
  return max(results)[1]

