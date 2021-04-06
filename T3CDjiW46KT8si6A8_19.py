
def product(lst):
​
  set_lst = set(lst)
​
  if len(set_lst) == 1:
    return max(set_lst) * max(set_lst)
  
  first_num = max(set_lst)
  set_lst.remove(first_num)
  second_num = max(set_lst)
​
  return first_num * second_num

