
def is_pandigital(n):
  a=[]
  while(n>0):
    b=n%10
    a.append(b)
    n=n//10
  s=set(a)
  l=list(s)
  e=[0,1,2,3,4,5,6,7,8,9]
  
  if l==e:
    return True
  else :
    return False

