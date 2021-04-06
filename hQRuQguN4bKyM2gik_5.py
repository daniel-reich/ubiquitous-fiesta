
def simple_check(a, b):
  a,b = max(a,b),min(a,b)
  total = 0
  for i in range(b):
    total+=(a%b==0)
    a-=1
    b-=1
  return total

