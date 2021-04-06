
def is_val_in_tree(tree, val):
  return any(is_val_in_tree(i, val) if type(i) is list else i == val for i in tree)

