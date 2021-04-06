
from collections import OrderedDict
def advanced_sort(lst):
  dic  = OrderedDict()
  b = []
​
  for i in range(len(lst)):
    dic[lst[i]] = dic.get(lst[i],0) + 1
    
  for key, values in dic.items():
    b.append([key]*values)
  return b

