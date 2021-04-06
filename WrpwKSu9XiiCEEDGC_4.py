
def can_alternate(s):
  a=0
  b=0
  
  for x in s:
    if x =='1':
      a+=1
    else:
      b+=1
  print(a,b)
  if a+1 == b or b+1 ==a or a== b:
    return True
  else:
    return False

