
def leader(lst):
  ans = []
  for i in range(len(lst)-1):
    a=True
    for j in range(i+1,len(lst)):
      if lst[i]<=lst[j]:
        a=False
        break
    if a==True:
      ans.append(lst[i])
      
  ans.append(lst[-1])
  return ans

