
def relation_lst(lst):
  return [(a,b) for a in sorted(lst) for b in sorted(lst) if b>=a]

