
def filter_list(lst):
  num_lst =[]
  for item in lst:
    if not type(item) == str:
      num_lst.append(item)
  return num_lst

