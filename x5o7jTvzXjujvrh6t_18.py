
def i_sqrt(n):
  if n<0:
    return 'invalid'
  if n<=2:
    return n-1
  cnt = 0
  while n>=2:
    n = n**0.5
    cnt+=1
  return cnt

