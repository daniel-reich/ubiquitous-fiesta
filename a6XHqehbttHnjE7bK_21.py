
def is_repdigit(num):
  if num<0:
    return False
  
  a=[]
  while(num>0):
    b=num%10
    num=num//10
    a.append(b)
  c=set(a)
  
  if len(c)==1:
    return True
  return False

