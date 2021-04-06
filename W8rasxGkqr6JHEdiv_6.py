
from itertools import permutations,product
def countdown(operands, target):
  n = len(operands)
  for p in permutations([str(k) for k in operands], n):
    for q in product(*[['+','-','*','//']]*(n-1)):
      exp = ''.join([[p,q][i%2][i//2] for i in range(2*n-1)])
      if eval(exp) == target:
        return exp
  return str(target)

