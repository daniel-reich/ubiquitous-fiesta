
def is_disarium(n):
  a=str(n)
  c=0
  sum=0
​
  for i in a:
    c=c+1
    sum=sum+int(i)**c
  
  if sum==n:
    return True
  else:
    return False

