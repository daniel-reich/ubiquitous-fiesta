
def sorting_steps(l):
  steps=[]
  for i in range(len(l)):
    j=l.index(min(l[i:]),i)
    if j!=i:
      steps+=[(i,j)]
      l[i],l[j]=l[j],l[i]
  return steps

