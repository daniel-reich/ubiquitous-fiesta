
def sort_array(lst):
  
  swaps = True
  
  while swaps:
    swaps = False
    for i in range(1,len(lst)):
      if lst[i-1] > lst[i]:
        lst[i-1], lst[i] = lst[i], lst[i-1]
        swaps = True
        
  return lst

