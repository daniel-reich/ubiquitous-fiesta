
def is_anti_list(lst1, lst2):
  same = set(lst1) == set(lst2)
  if same:
    for i in range(len(lst1)):
      if lst1[i] == lst2[i]:
        return False
    return True
  else:
    return False

