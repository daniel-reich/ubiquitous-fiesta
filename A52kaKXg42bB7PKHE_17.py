
from numbers import Number
​
def num_then_char(lst):
  all_elements = [element for l in lst for element in l]
  nums = list(filter(lambda x: isinstance(x, Number), all_elements))
  chars = list(filter(lambda x: type(x) == str, all_elements))
  nums.sort()
  chars.sort()
  sorted_list = nums + chars
  
  counter = 0
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      lst[i][j] = sorted_list[counter]
      counter += 1
  
  return lst

