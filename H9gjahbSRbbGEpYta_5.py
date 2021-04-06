
def multiply(n1, n2): 
  if n1<0:
    return multiply(-n1,-n2)
  ans = 0
  for _ in range(n1):
    ans+= n2
  return ans

