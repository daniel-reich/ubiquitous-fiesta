
def adjacent_product(lst):
  
  for i in range(len(lst)-1):
    if i == 0:
      highest = lst[i] * lst[i+1]
    elif lst[i] * lst[i+1] > highest:
      highest = lst[i] * lst[i+1]
    
  return highest

