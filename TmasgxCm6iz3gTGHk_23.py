
def exceeds(lst,k,n):
  sublist = list(map(lambda x: sum(lst[x:x+k]),range(0,len(lst)-k+1)))
  return max(sublist) > n
    
​
def min_length(lst, n):
  for i in range(1,len(lst)+1):
    if exceeds(lst,i,n):
      return i
  return -1

