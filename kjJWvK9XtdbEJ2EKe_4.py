
def sort_array(l):
  m=len(l)
  for i in range(m-1):
    for j in range(i+1,m):
      if l[i]>l[j]:l[i],l[j]=l[j],l[i]
  return l

