
def larger_than_right(lst):
  if(len(lst)==0):
    return lst
  ans=list()
  for i in range(0,len(lst)):
    check=0
    for j in range(i+1,len(lst)):
      if(lst[i]<=lst[j]):
        check=1
        break
    if(check==0):
      ans.append(lst[i])
  return ans

