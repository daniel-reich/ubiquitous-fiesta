
def num_of_sublists(lst):
  list_count = 0
  
  for item in lst:
    if type(item) is list:
      list_count += 1
      
  return list_count

