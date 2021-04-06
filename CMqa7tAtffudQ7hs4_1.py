
def sorting_steps(l):
  s=[]
  for i in range(len(l)-1):
    for j in range(i,len(l)):
      if l[i]>l[j]:
        s.append((i,j))
        l[i],l[j]=l[j],l[i]
  return s

