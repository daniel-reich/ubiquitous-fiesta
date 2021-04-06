
import itertools
def countdown(operands, target):
  for ops in itertools.product(['+', '-', '*', '//'], repeat=len(operands) - 1):
    for item in itertools.permutations(operands, len(operands)):
      formula = [str(item[0])]
      for op, operand in zip(ops, item[1:]):
        formula.extend([op, str(operand)])
      formula = ' '.join(formula)
      if eval(formula) == target and all([str(i) in formula for i in operands]):
        return formula

