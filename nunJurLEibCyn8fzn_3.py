
def filter_list(lst):
  all_num = []
  
  for i in lst:
    if type(i) == int:
      all_num.append(i)
    else:
      pass
  return all_num

