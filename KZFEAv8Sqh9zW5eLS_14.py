
def is_val_in_tree(tree, val):
  for item in tree:
    if type(item) is list:
      if is_val_in_tree(item, val):
        return True
    elif item == val:
      return True
  return False

