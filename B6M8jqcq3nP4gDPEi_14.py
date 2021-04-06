
def iso_group(lst,m=[float('-inf')]):
  if not lst:
    return m[0] if len(m) == 1 else m
  if lst[0] == m[0]:
    m.append(lst[0])
  elif lst[0] > m[0]:
    m = [lst[0]]
  return iso_group(lst[1:],m)

