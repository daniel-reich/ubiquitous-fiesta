
def simple_check(a, b):
  k = 0
  while (a>0 and b>0):
    if (a%b==0 or b%a==0):k+=1
    a-=1
    b-=1
  return k

