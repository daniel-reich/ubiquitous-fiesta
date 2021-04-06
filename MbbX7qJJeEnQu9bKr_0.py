
from collections import*
def max_occur(t):
  d=Counter(t).most_common()
  m=d[0][1]
  if m==1:return'No Repetition'
  l=[d[0][0]]
  for x in d[1:]:
    if x[1]!=m:break
    l.append(x[0])
  return sorted(l)

