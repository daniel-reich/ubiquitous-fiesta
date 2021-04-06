
def find_fulcrum(l, k=1):
  if k == len(l) - 1: return -1
  return l[k] if sum(l[:k]) == sum(l[k+1:]) else find_fulcrum(l, k+1)

