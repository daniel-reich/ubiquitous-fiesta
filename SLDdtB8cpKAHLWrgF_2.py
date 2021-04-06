
from itertools import permutations
import re
def greater_permutation(expr, nums):
  def express(perm):
    expression = expr
    for a,b in zip(perm,['a','b','c']):
      expression = expression.replace(b,str(a))
    return expression
  def result(perm):
    string = express(perm)
    while True:
      if not "(" in string:
        return eval(string)
      string = re.sub(r'(\()([^\(\)]+)(\))',lambda x: str(eval(x.group(2))),string)
  perms = sorted(list(permutations(nums)),key = lambda x: result(x))
  n = result(perms[-1])
  if isinstance(n,int):
    s = str(n)
  elif bool(re.search(r'\.0$',str(n))) == True:
    s = re.sub(r'\.0$','',str(n))
  else:
    s = str(round(n,2))
  return "{} = {}".format(express(perms[-1]),s)

