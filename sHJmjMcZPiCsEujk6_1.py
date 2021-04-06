
def pilish_string(t):
  r,l=[],0
  for x in'314159265358979':
    s=t[l:l+int(x)]
    l+=int(x)
    if s:
      d=l-len(t)
      if d:s+=s[-1]*d
      r.append(s)
  return' '.join(r)

