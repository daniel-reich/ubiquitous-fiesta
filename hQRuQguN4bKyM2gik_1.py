
def simple_check(a, b):
  a, b = max(a,b), min(a,b)
  ans = 0
  
  while b>0:
    if a%b == 0: ans += 1
    a -= 1
    b -= 1
  
  return ans

