
def num_of_sublists(lst):
  count=0
  for i in lst:
    if isinstance(i,list):
      count+=1
  return count

