
def find_adjacent(lst):
  for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
      j=i+2
      while j<len(lst) and lst[i] == lst[j] :
        j=j+1
      del lst[i:j]
      return True
  return False
def final_result(lst):
  while(find_adjacent(lst)):
    pass
  else:
    return lst

