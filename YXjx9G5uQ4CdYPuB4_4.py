
def simple_comp(lst1, lst2):
  if lst1 == []:
    return True if lst2 == [] else False
  if lst2 == []:
    return False
  lst1 = [i*i for i in lst1]
  for i in range((len(lst1+lst2))//2):
    lst1.append(lst1.pop(0))
    if lst1 == lst2:
      return True
  return False

