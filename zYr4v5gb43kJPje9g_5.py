
def moving_partition(lst):
  new_lst=[]
  for i in range(len(lst)-1):
    new_lst.append([lst[:i+1],lst[i+1:]])
  return new_lst

