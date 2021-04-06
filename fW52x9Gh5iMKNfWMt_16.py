
def recaman_index(n):
  i=0
  l=[0]
  while i<7300:
    x=l[-1]-len(l)
    y=l[-1]+len(l)
    if x>=0 and x not in l:
        l.append(x)
    else:   
      if y>=0:
        l.append(y)
    i+=1
  return l.index(n)

