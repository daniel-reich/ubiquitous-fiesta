
def unique_lst(lst):
  lst1=[]
  for i in lst:
    if i >0 and i not in lst1:
      lst1.append(i)
  return lst1

