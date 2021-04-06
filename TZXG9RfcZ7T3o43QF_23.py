
from itertools import groupby 
​
def same_length(txt):
  one = []
  
  lst = [(label, sum(1 for _ in group)) for label, group in groupby(txt)]
  for i in lst:
    if i[0] == '1':
      one.append(i[1])
    elif one[0] != i[1] or len(lst) % 2 == 1:
      return False
    else:
      one = []
  return True

