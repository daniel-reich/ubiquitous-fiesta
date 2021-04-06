
def same_letter_pattern(txt1, txt2):
  l={}
  s=[]
  d={}
  y=[]
  c=0
  e=0
  for t in txt1:
    if t in l.keys():
      s.append(l[t])
    else:
      l[t]=c
      s.append(c)
      c+=1
  for p in txt2:
    if p in d.keys():
      y.append(d[p])
    else:
      d[p]=e
      y.append(e)
      e+=1
  if s==y:
    return True
  else:
    return False

