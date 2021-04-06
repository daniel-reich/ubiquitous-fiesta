
def is_anti_list(lst1, lst2):
  same_elems = set(lst1) == set(lst2)
  if same_elems:
    for i in range(0,len(lst1)):
      if lst1[i] == lst2[i]:
        return False
    return True
  else:
    return False

