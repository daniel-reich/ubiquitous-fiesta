
from collections import Counter as C
def longest_palindrome(s):
  d=dict(C(s))
  lp=0
  for x in d:
    if d[x]%2==0:
      lp+=d[x]
    else:
      lp+=d[x]-1
  lp+=1*any(d[x]%2 for x in d)  
  return lp

