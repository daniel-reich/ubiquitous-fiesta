
def find_fulcrum(lst):
  for i, x in enumerate(lst[1:-1]):
    if sum(lst[:i+1]) == sum(lst[i+2:]):
      return lst[i+1]
  return -1

