
def sort_array(lst):
  for i in range(len(lst)):
    for x in range(i,len(lst)):
      if lst[x] < lst[i]:
        lst[x],lst[i] = lst[i],lst[x]
  return lst

