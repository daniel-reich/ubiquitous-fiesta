
def is_isomorphic(s, t):
  return structure(s)==structure(t)
  
def structure(s):
  d,ret,it = {},'',0
  for i in s:
    if i not in d:
      d[i]=it
      ret+=str(d[i])
      it+=1
    else:
      ret+=str(d[i])
  return ret

