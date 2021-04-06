
def is_anti_list(lst1, lst2):
  print(lst1,lst2)
  for i in range(len(lst1)):
    if set(lst1) == set(lst2):
      return lst1[i] != lst2[i]
    else:
      return False

