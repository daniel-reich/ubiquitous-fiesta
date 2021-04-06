
def find_fulcrum(lst):
  for i, l in enumerate(lst):
    if sum(lst[:i]) == sum(lst[i+1:]): return l
  return -1

