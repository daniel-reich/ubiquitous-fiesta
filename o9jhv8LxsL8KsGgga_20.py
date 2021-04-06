
def bound_sort(lst, bounds):  
  l1=sorted(lst[bounds[0]:bounds[-1]+1])+lst[bounds[-1]+1:len(lst)]
  
  #print(lst[bounds[0]:bounds[-1]+1],l1)  
  if sorted(lst)==l1:
    return True
  else: 
    return False

