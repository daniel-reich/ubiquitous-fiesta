
def final_result(lst):
  i=0
  while i < len(lst):
    delete = 0
    j = i+1
    while j < len(lst) and lst[j] == lst[i]:
      delete+=1
      j+=1
    if delete:
      for d in range(delete+1):
        del lst[i]
      i = 0
    else:
      i+=1
  return lst

