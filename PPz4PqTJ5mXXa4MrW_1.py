
def ulam(n):
  a=[1,2]
  s=set(a)
  for i in range(3,n*12):
    count=0
    for j in range(0,len(a)):
      if i-a[j]in s and a[j]!=i-a[j]:count+=1
      if count>2:break
    if count==2:a.append(i);s.add(i)
  return a[n-1]

