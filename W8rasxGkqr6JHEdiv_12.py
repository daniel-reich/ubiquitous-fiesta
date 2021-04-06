
import itertools as it
​
def countdown(operands, target):
  operands = it.permutations(operands,len(operands))
    
  for operands_test in operands:
    operators = it.product({'+','-', '*', '//'},repeat = len(operands_test) - 1)
    for operators_test in operators:
      test = ''.join([str(a) + b for a,b in zip(operands_test,operators_test + ('',))])
      if eval(test) == target:
        return test
  return 'Failed'

