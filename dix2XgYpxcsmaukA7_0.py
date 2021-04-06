
from collections import*
def express_factors(n):
  p,l,s=2,[],''
  while n>=p*p:
    if n%p:p+=1
    else:l.append(p);n/=p
  l.append(int(n))
  for k,v in sorted(Counter(l).items()):
    s+=(' x ','')[s=='']+str(k)
    if v>1:s+='^'+str(v)
  return s

