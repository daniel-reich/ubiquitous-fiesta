
def is_val_in_tree(tree, val):
  while tree:
    if val in tree:
      return True
    tree = sum([i for i in tree if isinstance(i, list)],[])
  return False

