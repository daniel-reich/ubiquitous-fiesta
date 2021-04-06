
def deepest(lst, depth=1):
  return max((deepest(i, depth+1) for i in lst if type(i) is list), default=depth)

