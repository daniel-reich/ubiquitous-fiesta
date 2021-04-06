
def tree(h):
  max_width = (h - 1) * 2 + 1
  tree = []
  for i in range(1, h + 1):
    tree_part = "#" * ((i - 1) * 2 + 1)
    padding = " " * ((max_width - len(tree_part)) // 2) 
    tree.append(padding + tree_part + padding)
  return tree

