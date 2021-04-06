
def tree(h):
  chtree = []
  for i in range(h):
    chtree.append(("#" * (i * 2 + 1)).center(h * 2 - 1))
  return chtree

