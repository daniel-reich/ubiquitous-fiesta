
def is_val_in_tree(tree, val):
  list1 = []
​
  for x in tree:
    list1.append(x)
  
  # If anything in the list is a sublist, add everything in the sublist to the list.
  while True:
    for x in list1:
      if type(x) == list:
        for y in x:
          list1.append(y)
        continue
    break
  
  # If anything in the list is a list, delete it.
  for x in list1:
    if type(x) == list:
      del x
  
  for x in list1:
    if x == val:
      return True
  
  return False

