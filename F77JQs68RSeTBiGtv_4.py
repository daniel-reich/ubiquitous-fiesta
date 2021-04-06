
def diamond_sum(n):
  lst = [[j for j in range(i,i+n)] for i in range(1,n**2+1,n)]
  ret = 0
  x,y = n//2,n//2
  for i in range(n):
    if i==0 or i==n-1:
      ret+=lst[i][x]
    else:
      ret+=lst[i][x]+lst[i][y]
    if i<n//2:
      x-=1
      y+=1
    else:
      x+=1
      y-=1
  return ret

