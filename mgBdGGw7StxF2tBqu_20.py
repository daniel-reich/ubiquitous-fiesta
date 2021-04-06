
def duplicates(txt):
  c=0
  d=[]
  for i in txt:
    if i in d: pass
    else:
      a=0
      a=txt.count(i)
      if a>1:c=c+(a-1)
      d.append(i)
  return c

