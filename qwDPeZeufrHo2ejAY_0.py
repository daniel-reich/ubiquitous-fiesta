
def eval_algebra(eq):
  right = eq.index('x') > eq.index('=')
  negative = '- x' in eq
  eq = eq.replace('x','0').split('=')
  value = eval(eq[1])-eval(eq[0])
  return value*(-1)**(right+negative)

