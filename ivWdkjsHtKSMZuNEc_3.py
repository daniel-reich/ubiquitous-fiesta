
import re
​
def find_shortest_words(txt):
  res=[]
  ls=re.findall(r"[a-zA-Z']+",txt)
  minLen=len(txt)+1
  for x in ls:
    if len(x)<minLen:
      res=[x.lower()]
      minLen=len(x)
    elif len(x)==minLen:
      res.append(x.lower())
  res.sort()
  return res

