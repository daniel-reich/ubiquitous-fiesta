
import numpy as np
def sort_by_letter(lst):
​
  
  list2 =[]
  list3 =[]
  for i in range(len(lst)):
      for j in lst[i]:
          if j.isalpha():
              list2.append(j)
​
  idx = np.argsort(list2)
​
  for i in idx:
      list3.append(lst[i])
  return list3

