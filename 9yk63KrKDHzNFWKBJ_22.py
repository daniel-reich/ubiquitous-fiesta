
def is_it_inside(tree, tar, fol):
  if tar == fol or tar in tree.get(fol,[]):
    return True       
  for f in list(tree.get(fol,[])):
    if f in tree:
      is_it_inside(tree,tar,f)
    if f not in tree:
      tree[fol].remove(f)
  if fol in tree and not tree[fol]:
    del tree[fol]
  return fol in tree

