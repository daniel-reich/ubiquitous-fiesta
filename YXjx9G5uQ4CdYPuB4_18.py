
def simple_comp(lst1, lst2):
  if lst1==[] and lst2==[]:
    return True
  return isinstance(lst1,list) and isinstance(lst2,list) and len(lst1)>0 and all([lst2.count(i**2)==lst1.count(i) for i in lst1])

