
def remove_smallest(lst):
  if lst==[]:
    return lst
  lowest= None
  for num in lst:
    if lowest == None:
      lowest = num
    if lowest>num:
      lowest = num
  del lst[lst.index(lowest)]
  return lst

