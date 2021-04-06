
from itertools import combinations
def combo_list(lst,n,k):
  newlst = list(map(lambda x: sorted(list(x)),combinations(lst,n)))
  newlst = list(filter(lambda x: sum(x) == k,newlst))
  newlst.sort(key = lambda x: x[0])
  return newlst
  
def get_subsets(lst, n):
  newlst = []
  for i in range(1,len(lst)+1):
    newlst.extend(combo_list(lst,i,n))
  return newlst

