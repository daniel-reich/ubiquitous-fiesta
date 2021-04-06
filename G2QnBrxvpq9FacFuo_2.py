
def possible_path(lst):
  count = 0
  if len(lst)>1:
    for i in lst[1:]:
      if isinstance(i,int) and isinstance(lst[count], int) or isinstance(i,str) and isinstance(lst[count],str):
        return False
      count += 1
  return True

