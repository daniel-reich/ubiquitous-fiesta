
def divide(lst, n):
  ans=[]
  start=0
  for i in range(len(lst)+1):
    if sum(lst[start:i+1]) > n:
      ans.append(lst[start:i])
      start = i
  ans.append(lst[start:])
  return ans

