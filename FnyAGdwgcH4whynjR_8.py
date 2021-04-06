
from itertools import combinations
​
def get_subsets(lst, n):
  sum_lst = []
  for sl_lenght in range(1, len(lst) + 1):
    for sub_list in list(combinations(lst, sl_lenght)):
      sum = 0
      for num in sub_list:
        sum += num
      if sum == n:
        sum_lst.append(sorted(sub_list))
  return sum_lst

