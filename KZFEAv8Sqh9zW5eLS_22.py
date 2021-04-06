
def is_val_in_tree(tree, val):
  import re
  lst=[int(c) for c in re.findall(r'\d+(?:,\d+)?',str(tree)) if c.isnumeric()]
  return [True if val in lst else False][0]

