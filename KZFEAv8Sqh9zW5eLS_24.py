
def is_val_in_tree(tree, val):
  for i in tree:
    if type(i) is list:
      if is_val_in_tree(i, val):
        return True
    elif val == i:
      return True
  return False

