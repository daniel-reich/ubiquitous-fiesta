
def antipodes_average(lst):
  if not lst:
    return None
  left_list, right_list = split_list(lst)
  return get_divid_sum_list(left_list, right_list)
  
  
def split_list(lst):
  l = len(lst)
  if l % 2 == 0:
    return lst[0:l//2], lst[l//2:l]
  else:
    return lst[0:(l-1)//2], lst[(l+1)//2:l]
    
def get_divid_sum_list(left_list, right_list):
  res = []
  l = len(left_list)
  for i in range(l):
    res.append((left_list[i] + right_list[l - 1 - i]) / 2)
  return res

