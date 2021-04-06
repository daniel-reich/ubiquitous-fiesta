
def mathematical(exp, numbers):
  return ['f({})={}'.format(y,int(eval(exp[5:].replace('^','**').replace('x','*')))) for y in numbers]

