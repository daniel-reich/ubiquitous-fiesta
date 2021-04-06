
def unique_lst(lst):
  lst2 = [num for num in lst if num > 0]
  lst3 = []
  
  for num in lst2:
    if num not in lst3:
      lst3.append(num)
      
  return lst3

