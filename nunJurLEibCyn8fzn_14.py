
def filter_list(lst):
  new_lst = []
  for ele in lst:
    if isinstance(ele,int):
      new_lst.append(ele)
  return new_lst

