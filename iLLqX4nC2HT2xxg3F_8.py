
def deepest(lst):
  if not isinstance(lst, list):
    return 0
  else:
    return max(map(deepest, lst)) + 1

