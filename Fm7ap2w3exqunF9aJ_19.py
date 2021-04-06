
def count_lone_ones(n):
  x=str(n)
  a=[]
  count=0
  for i in x:
    a.append(int(i))
  a.append(0)
  for i in range(len(a)-1):
    if a[i]==1 and a[i+1]!=1 and a[i-1]!=1:
      count+=1
  return(count)

