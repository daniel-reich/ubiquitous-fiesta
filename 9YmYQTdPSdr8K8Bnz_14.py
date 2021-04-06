
def unique_lst(lst):
  lst2=[]
  for num in lst:
    if num>0 and num not in lst2:
      lst2.append(num)
  return lst2

