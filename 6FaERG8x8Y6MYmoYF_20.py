
from collections import Counter as C
def dice_score(throw):
  d=dict(C(throw))
  p=0
  for x in d:
    if x==1:
      p+=divmod(d[x], 3)[0]*1000+divmod(d[x], 3)[1]*100
    elif x==5:
      p+=divmod(d[x], 3)[0]*500+divmod(d[x], 3)[1]*50
    else:
      p+=divmod(d[x], 3)[0]*x*100
  return p

