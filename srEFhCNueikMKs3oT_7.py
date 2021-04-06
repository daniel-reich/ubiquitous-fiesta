
def consecutive_sum(n):
  A=[]
  for i in range(1, n//2+1):
    s=0
    while s<n:
      s+=i
      i+=1
    if s==n:
      return True
  return False

