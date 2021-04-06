
from collections import Counter
def advanced_sort(lst):
  x= {val:[val]*count for val,count in Counter(lst).items()}
  y = []
  z = []
  for i in lst:
    if i not in z:
      y.append(x[i])
      z.append(i)
  return y

