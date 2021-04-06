
def grant_the_hint(txt):
  s=[]
  for k in range(-1, max([len(i) for i in txt.split()])):
    l=[]
    for i in txt.split():
      d=""
      for j in range(len(i)):
        if j > k:
          d+='_'
        else:
          d+=i[j]
      l.append(d)
    s.append(" ".join(l))
  return s

