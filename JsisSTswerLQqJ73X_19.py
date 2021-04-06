
def priority_sort(lst, s):
  l=[]
  for x in lst:
    if x in s:  
      l.append(x)
  for y in l:
    lst.remove(y)
  l.sort()
  lst.sort()
  for z in lst:
    l.append(z)
  return l

