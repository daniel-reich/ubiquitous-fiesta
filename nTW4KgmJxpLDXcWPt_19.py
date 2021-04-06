
def move_to_end(lst, el):
  remove_count = 0
  for index in range(len(lst)-1,-1,-1):
    if(lst[index] == el):
      remove_count += 1
      lst.pop(index)
    
  while(remove_count > 0):
    lst.append(el)
    remove_count -= 1
    
  return lst

