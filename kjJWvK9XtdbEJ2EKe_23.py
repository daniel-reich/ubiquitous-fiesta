
def sort_array(lst):
  f_list = []
  for ind in range(0,len(lst)):
    minn = min(lst)
    f_list.append(minn)
    lst.remove(minn)
  return f_list

