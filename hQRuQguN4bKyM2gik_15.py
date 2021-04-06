
def simple_check(a, b):
  c = 0
  if a < b:
    a,b=b,a
  while b>0:
    
    if a%b == 0:
      c +=1
    a-=1
    b-=1
    
    
  return c

