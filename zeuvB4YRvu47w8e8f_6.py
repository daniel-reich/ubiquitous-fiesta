
def full_cycle(lst):
  visited = []
  if len(set(lst)) < len(lst):
    return False
  if any(lst[i] == i for i in range(0,len(lst))):
    return False
  if max(lst) >= len(lst):
    return False
  i = 0
  while len(visited) < len(lst)-1:
    visited.append(i)
    if lst[i] in visited:
      return False
    i = lst[i]
  return True

