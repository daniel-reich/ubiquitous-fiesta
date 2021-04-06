
from operator import itemgetter
def factor_sort(nums):
  lst = [factor_len(x) for x in nums]
  lst = sorted(lst, key = itemgetter(1,0),reverse = True)
  res = [lst[i][0] for i in range(len(lst))]
  return res
  
  
  
​
​
def factor_len(n):
  return [n, len([x for x in range(1,n+1) if n%x==0])]

