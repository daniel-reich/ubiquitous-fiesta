
def advanced_sort(lst):
  new_lst = []
  for i in lst:
    if [i]*lst.count(i) not in new_lst:
       new_lst.append([i]*lst.count(i))
  return (new_lst)

