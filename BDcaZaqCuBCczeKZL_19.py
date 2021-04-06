
def arrow(num):
  ans=[]
  if num%2:
    for i in range(1,num+1):
      ans.append('>'*i)
    for j in range(num-1,0,-1):
      ans.append('>'*j)
  else:
    for i in range(1,num+1):
      ans.append('>'*i)
    for j in range(num,0,-1):
      ans.append('>'*j)   
  return ans

