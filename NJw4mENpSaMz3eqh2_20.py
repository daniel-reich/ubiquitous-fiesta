
def is_undulating(n):
 x=str(n)
 if len(x)<3:
  return False
 if len(x)%2==0:
  if x.count(x[0])!=len(x)/2 or x.count(x[1])!=len(x)/2:
   return False
 if len(x)%2==1:
  if len(x)-x.count(x[0])!=1 or len(x)-x.count(x[1])!=2:
   return False
 for i in range(len(x)):
  if i!=len(x)-1:
   if x[i]==x[i+1]:
    return False
 return True

