
def junction_or_self(n):
  arr=[]
  for i in range(1,n):
    sum=0
    k=str(i)
    for j in k:
      sum=int(j)+sum
    total=sum+i
    if(total==n):
      arr.append(i)
  if(arr==[]):
    return('Self')
  else:
    s=sorted(arr,reverse=True)
    return(s)

