
def mathematical(exp, numbers):
  exp = exp[5:].replace('x','*').replace('^','**')
  return ['f('+str(n)+')='+str(int(eval(exp.replace('y',str(n))))) for n in numbers]

