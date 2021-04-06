
def complete_bracelet(lst):
  a=[lst[0]]
  d=[]
  for i in range(1,len(lst)):
    a.append(lst[i])
    b=lst[i+1:(2*i)+2]
    if a==b:
      d=b
  e=[]
  c=0
  for i in lst:
    e.append (i)
    if d==e:
      c+=1
      e=[]
  return len(lst)==c*len(d)

