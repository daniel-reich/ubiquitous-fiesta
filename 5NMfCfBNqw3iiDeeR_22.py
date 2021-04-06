
def sum_minimums(lst):
  min_lst = [] 
  
  for i in lst:
    min_lst.append(min(i))
  
  return sum(min_lst)

