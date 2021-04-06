
def pairwise_swap(lst):
  if not lst: return[]
    
  for i in range(0, len(lst)-1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
  
  if len(lst) % 2:
    ascii_val = lambda w: sum(ord(c) for c in str(w))
    
    ascii_max, ascii_max_index = 0, 0
    for i,v in enumerate(lst):
      asc = ascii_val(v)
      if asc > ascii_max:
        ascii_max, ascii_max_index = asc, i
    lst[-1], lst[ascii_max_index] = lst[ascii_max_index], lst[-1]
  
  return lst

