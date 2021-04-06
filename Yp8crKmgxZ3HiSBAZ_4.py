
def freq_count(l,e):
  r,s=[],[]
  c=i=0
  while l:
    for x in l:
      if isinstance(x,list):s.extend(x)
      elif x==e:c+=1
    r.append([i,c])
    c,i=0,i+1
    l.clear()
    while s:l.append(s.pop())
  return r

