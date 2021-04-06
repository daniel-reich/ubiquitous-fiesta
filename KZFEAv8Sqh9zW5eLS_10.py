
def is_val_in_tree(tree, val):
  v, left, right = tree
  if v == val:
    return True
  find = False
  for child in (left, right):
    if child:
      find = find or is_val_in_tree(child, val)
  return find

