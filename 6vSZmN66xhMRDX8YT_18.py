
from collections import Counter
def advanced_sort(lst):
  result=list()
  x=Counter(lst)
  included=list()
  for i in lst:
    if(i not in included):
      a=list()
      included.append(i)
      for j in range(0,x[i]):
        a.append(i)
      result.append(a)
  return result

