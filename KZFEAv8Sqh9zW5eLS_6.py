
def is_val_in_tree(tree, val):
  if tree == [] or tree == None: return False
  if tree[0]==val: return True
  
  return is_val_in_tree(tree[1],val) or is_val_in_tree(tree[2],val)

