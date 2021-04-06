
def diamond_sum(n):
  out=0
  for i in range(n):
    m=i*n + n//2 +1
    o=i if i<n//2 else n-i-1
    out+=m-o
    if o>0:out+=m+o
    
  return out

