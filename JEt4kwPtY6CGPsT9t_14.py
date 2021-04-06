
def mathematical(exp, numbers):
  exp = exp.replace('^','**').replace('x','*').replace('/','//')
  exps = [exp.replace('y', str(n)).split('=') for n in numbers]
  return ['='.join([L,str(eval(R))]) for [L,R] in exps]

