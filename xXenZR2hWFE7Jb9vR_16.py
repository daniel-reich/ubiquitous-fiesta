
def is_isomorphic(s, t):
  
  d1 = dict() 
  l1 = []
  c = 0
  for i in range(0,len(s)):
    if s[i] in d1:
      l1.append(d1[s[i]])
    else:
      l1.append(c)
      d1[s[i]]=c
      c+=1
  
  d2 = dict() 
  l2 = []
  c = 0
  for i in range(0,len(t)):
    if t[i] in d2:
      l2.append(d2[t[i]])
    else:
      l2.append(c)
      d2[t[i]]=c
      c+=1
  return l1==l2

