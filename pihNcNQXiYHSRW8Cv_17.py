
def sort_by_length(lst):
  if len(lst) == 0:
    return []
​
  str_list = [lst[0]]
  
  for i in lst[1:]:
    idx = -1
    for j in str_list:
      idx += 1
      if len(i) < len(j):
        str_list.insert(idx,i)
        break
      if len(str_list) == (idx+1):
        str_list.insert(idx+1,i)
        break
  
  return str_list

