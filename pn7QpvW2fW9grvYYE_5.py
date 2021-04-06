
def find_fulcrum(lst):
  for i in range(1, len(lst)-1):
    if sum(lst[:i]) == sum(lst[i+1:]):
      return lst[i]
  return -1

