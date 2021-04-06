
def is_val_in_tree(tree, val):
  return str(val) in ''.join(c if c.isdigit() else ' ' for c in str(tree)).split()

