
def is_unprimeable(num):
  y=[]
  if(p(num)): 
    return "Prime Input"
  s=str(num)
  t=[0,1,2,3,4,5,6,7,8,9]
  for i in range(0,len(s)):
    for k in t:
      h=int(s[0:i]+str(k)+s[i+1:])
      print(h)
      if(p(h)):
        y.append(h)
  if(y==[]):
    return 'Unprimeable'
  else:
    return sorted(y)
def p(n):
  t=0
  for i in range(1,int((n/2))+1):
    if(n%i==0):
      t+=1
  return t==1

