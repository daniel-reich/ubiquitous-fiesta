
def diamond_arrays(x):
  ans=[]
  for i in range(1,x+1):
    ans.append([i]*i)
  for i in range(x-1,0,-1):
    ans.append([i]*i)
  return ans

