
import re
def bird_code(lst):
  A=[re.split('[\-\s]',x) for x in lst]
  B=[]
  for x in A:
    if len(x)==1:
      B.append(x[0][:4].upper())
    elif len(x)==2:
      B.append((x[0][:2]+x[-1][:2]).upper())
    elif len(x)==3:
      B.append((x[0][0]+x[1][0]+x[2][:2]).upper())
    else:
      B.append((x[0][0]+x[1][0]+x[2][0]+x[3][0]).upper())
  return B

