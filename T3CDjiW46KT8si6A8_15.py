
def product(lst):
  lst = list(set(lst))
  lst.sort()
  if len(lst)==1:
    return lst[0]**2
  
    
  return lst[-1]*lst[-2]

