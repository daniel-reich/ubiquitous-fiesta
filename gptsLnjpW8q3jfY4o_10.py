
from math import factorial as f
def Formula(n):
  r = True if n < 0 else False
  n = abs(n)
  e = [str(f(n)//(f(i)*f(n-i))) + 'a^'+str(n-i) + 'b^'+str(i) for i in range(n+1)]
  e = 'X' + '+'.join(e) + 'X'
  e = e.replace('a^1b', 'ab').replace('b^1+', 'b+').replace('b^1X', 'b')
  e = e.replace('a^0', '').replace('b^0', '')
  e = e.replace('X1a', 'a').replace('+1b', '+b').replace('X', '')
  return  '1/(' + e + ')' if r else e

