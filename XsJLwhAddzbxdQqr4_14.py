
def difference_max_min(lst):
  ind = 0;
  smol = lst[0];
  thicc = lst[0];
  
  while ind < len(lst):
    if lst[ind] < smol:
      smol = lst[ind];
    elif lst[ind] > thicc:
      thicc = lst[ind];
    ind+=1;
    
  return thicc-smol;

