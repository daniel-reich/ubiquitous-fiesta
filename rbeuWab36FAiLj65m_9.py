
def grouping(w):
  d={}
  for i in w:
    x=0
    for j in i:
      if j.isupper():
        x+=1
    if x in d.keys():
      d[x].append(i)
      d[x].sort(key=lambda x:x.lower())
    else:d[x]=[i]
  return d

