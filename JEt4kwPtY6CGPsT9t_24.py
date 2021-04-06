
def mathematical(exp, numbers):
  expr = exp.replace('x','*').replace('^','**').replace('/','//')[5:]
  return ['f({})={}'.format(y, eval(expr)) for y in numbers]

