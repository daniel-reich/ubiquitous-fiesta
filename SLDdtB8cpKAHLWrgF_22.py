
from itertools import permutations as p
def greater_permutation(expr, nums):
​
  mx = 0
  s = ""
  for x in list(p(nums)):
    tmp = expr
    tmp = tmp.replace("a",str(x[0]))
    tmp = tmp.replace("b",str(x[1]))
    tmp = tmp.replace("c",str(x[2]))
    
    num = round(eval(tmp),2)
    if (1.0*num).is_integer():num = int(num)
    if num>=mx:
      mx = num
      s = tmp+" = "+str(num)
  return s

