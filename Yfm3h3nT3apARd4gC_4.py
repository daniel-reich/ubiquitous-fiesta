
def rolls(lst):
  return eval('+'.join(map(str,lst)).replace('1+','1+0*').replace('6+','6+2*'))

