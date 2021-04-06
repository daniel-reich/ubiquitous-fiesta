
def mathematical(exp, numbers):
  exp
  return ['f({})='.format(str(n))+str(int(eval(exp[5:].replace('y', str(n)).replace('^','**').replace('x','*')))) for n in numbers]

