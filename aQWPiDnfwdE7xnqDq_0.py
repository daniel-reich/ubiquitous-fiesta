
from math import*
def drange(*l):
  def f(e,s,t):
    p=max(map(lambda x:len(str(x))-len(str(trunc(x))),[e,s,t]))
    if p>0:p-=1
    while s<e:yield round(s,p);s+=t
  if len(l)<2:e,s,t=l[0],0,1
  elif len(l)==2:s,e,t=l[0],l[1],1
  else:s,e,t=l
  return tuple(f(e,s,t))

