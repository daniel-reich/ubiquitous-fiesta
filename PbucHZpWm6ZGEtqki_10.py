
import numpy as np
def sliding_sum(lst, n, k):
  final_lst = []
  for i in range(len(lst)-1):
    if sum(lst[i:i+n]) == k:
      final_lst.append(lst[i:i+n])
  if all(np.array(lst)==k) and n == 1:
    final_lst.append([lst[-1]])
    return final_lst
  else:
    return final_lst

