
def countdown(operands, target):
​
  def operators(amount):
  
    from itertools import product as pro
    
​
    operator_dicti = {1: '+', 2: '-', 3: '*', 4: '//'}
    operator_options = [p for p in pro([1,2,3,4], repeat = amount)]
​
    diff_operator_poss = []
​
    for option in operator_options:
      poss = []
      for op in option:
        poss.append(operator_dicti[op])
      diff_operator_poss.append(poss)
    
    return diff_operator_poss
  def operand_order(ops):
    from itertools import permutations as p
​
    return list(p(operands))
  
  o = operators(len(operands) - 1)
  oo = operand_order(operands)
​
  for integers in oo:
    for operators in o:
      s = ''
      ii = 0
      oi = 0
​
      for n in range(len(operands) * 2 - 1):
        if n % 2 == 0:
          s += '{}'.format(integers[ii])
          ii += 1
        else:
          s += '{}'.format(operators[oi])
          oi += 1
      
      if eval(s) == target:
        return s

