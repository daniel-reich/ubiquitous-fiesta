
def check_pattern(lst, pattern):
  d = {}
  for i in range(len(pattern)):
    if pattern[i] not in d.keys():
      d[pattern[i]] = tuple(lst[i])
      for j in d:
        if d[j] == tuple(lst[i]) and pattern[i] != j:
          return False
    else:
      if d[pattern[i]] != tuple(lst[i]):
        return False
  return True

