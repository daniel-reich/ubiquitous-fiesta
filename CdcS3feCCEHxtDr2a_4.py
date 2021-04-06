
from functools import reduce
​
def clear_ordering(lst):
  merged_list = [item.lower() for item in reduce(lambda a, b: a+b, lst)]
  l1 = [merged_list[item] for item in range(0, len(merged_list), 2)]
  l2 = [merged_list[item] for item in range(1, len(merged_list), 2)]
  
  for char in merged_list:
    if(l1.count(char) > 1 or l2.count(char) > 1):
      return False
  return True

