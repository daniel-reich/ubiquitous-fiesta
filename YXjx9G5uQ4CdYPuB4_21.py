
def simple_comp(lst1, lst2):
  if not lst1 or not lst2:
    return lst1==lst2
  for i in range(len(lst2)-1):
    good = True
    for a,b in zip(lst1,lst2):
      if a**2!=b:
        good = False
        break
    if good:
      return True
    lst2 = lst2[1:]+[lst2[0]]
  return False

