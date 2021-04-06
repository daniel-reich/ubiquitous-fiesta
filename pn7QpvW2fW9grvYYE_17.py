
def find_fulcrum(lst):
  if any(sum(lst[:i])==sum(lst[i+1:]) for i in range(len(lst))):
    for i in range(len(lst)):
      if sum(lst[:i])==sum(lst[i+1:]):
        return lst[i]
  else:
    return -1

