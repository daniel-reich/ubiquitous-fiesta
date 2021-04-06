
def mathematical(exp, numbers):
  f=exp.split('=')[1].replace('x','*').replace('^','**').replace('/','//')
  return ['f({})={}'.format(n,eval(f.replace('y',str(n)))) for n in numbers]

