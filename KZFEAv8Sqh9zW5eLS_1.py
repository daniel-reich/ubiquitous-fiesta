
def is_val_in_tree(tree, val):
  if not tree: return False
  if val in tree: return True
  return is_val_in_tree(tree[1], val) or is_val_in_tree(tree[2], val)

