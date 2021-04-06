
import re
def post_fix(expr):
  A=re.findall('\d\d?', expr)
  B=re.findall('[\+\-\*\/]', expr)
  C=[j for i in zip(A,B) for j in i]+[A[-1]]
  return eval(''.join(C))

