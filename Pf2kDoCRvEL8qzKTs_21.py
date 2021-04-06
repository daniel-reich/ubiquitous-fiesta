
def order_people(n,m):
  if(n[1]*n[0]<m):
    return "overcrowded"
  result=list()
  i=0
  k=1
  for i in range(0,n[0]):
    x=list()
    for j in range(0,n[1]):
      if(k<=m):
        x.append(k)
        k+=1
      else:
        x.append(0)
      
    result.append(x)
  for i in range(0,len(result)):
    check=0
    if(0 in result[i]):
      check=1
    for j in result[i]:
      if(check==1 and j>0):
        check=2
        break
    print(check)
    if(i%2!=0 and check<=1):
      result[i].sort(reverse=True)
    elif(i%2!=0 and check==2):
      result[i].reverse()
  return result

