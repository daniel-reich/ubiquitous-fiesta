
def recaman_index(n):
  l=[0]
  i = 0
  while l[i] != n: 
    s = l[-1]-len(l)
    a = l[-1]+len(l)
    if  s>=0 and s not in l:
      l.append(s)
    else:
      l.append(a)
    i += 1
  return i

