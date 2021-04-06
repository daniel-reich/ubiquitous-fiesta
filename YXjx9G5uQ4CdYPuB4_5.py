
def simple_comp(lst1, lst2):
  if lst1 and lst2:
    lst1 = sorted(lst1, key=abs)
    lst2 = sorted(lst2,key=abs)
    return all([i**2 == j for i,j in zip(lst1,lst2)]) 
    
  return lst1 == lst2

