
def eval_algebra(eq):
  eq='-'.join(eq.split('='))
  if '- x' in eq:return eval(eq.replace('x','0'))
  else:return -eval(eq.replace('x','0'))

