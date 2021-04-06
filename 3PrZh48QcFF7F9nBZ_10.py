
import re
def solver(eq):
  A=eq.split('=')
  leftc=eval(A[0].replace('x', '0'))
  rightc=eval(A[1].replace('x', '0'))
  eq2=eq.replace('x', '1x').replace(' ','').replace('*1x*1x','')
  B=eq2.split('=')
  p=r'[\d*?]+(?=x)'
  leftx=sum(eval(t.group()) for t in re.finditer(p,B[0]))
  rightx=sum(eval(t.group()) for t in re.finditer(p,B[1]))
  xc=leftx-rightx
  c=rightc-leftc
  if xc:
    return c/xc
  else:
    return "Infinite solutions"

