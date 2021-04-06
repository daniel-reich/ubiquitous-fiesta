
def maxmin(nn):
  nn=str(nn)
  n=list()
  for i in nn:
    n.append(i)
  result=list()
  result.append(int(nn))
  for i in range(0,len(n)):
    for j in range(i+1,len(n)):
      m=list()
      m.extend(n)
      x=m[j]
      m[j]=m[i]
      m[i]=x
      print(m)
      if(m[0]!='0'):
        result.append(int(''.join(m)))
      
  return (max(result),min(result))

