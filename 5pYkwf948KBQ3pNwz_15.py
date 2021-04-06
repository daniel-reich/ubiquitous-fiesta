
import re
from collections import Counter as C
def most_common_words(text, n):
  text=text.lower()
  p='\w+'
  A=re.findall(p,text)
  c=sorted(list(dict(C(A))), key=lambda x: (C(A)[x], -A.index(x)), reverse=True)
  res={}
  if n<len(A):
    for i in range(n):
      res[c[i]]=C(A)[c[i]]
    return res
  return C(A)

