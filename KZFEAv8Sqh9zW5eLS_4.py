
def is_val_in_tree(tree, val):
  if val in tree:
    return True
  return any([is_val_in_tree(i,val) for i in tree if isinstance(i,list)])

