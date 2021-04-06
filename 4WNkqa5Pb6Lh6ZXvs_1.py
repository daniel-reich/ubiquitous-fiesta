
import re
def evaluate_polynomial(p,n):
  try:
    if re.sub(r'[\dx+*-/()^]','',p):return'invalid'
    return eval(re.sub(r'(\d)([\(x])',r'\1*\2',p).replace('x(','x*(').replace('x',str(n)).replace('^','**').replace('//','k'))
  except:return'invalid'

