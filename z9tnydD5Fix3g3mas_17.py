
def check_pattern(lst, pattern):
  d = {}
  for i in range(len(lst)):
    if pattern[i] not in d:
      if lst[i] not in lst[:i]:
        d[pattern[i]] = lst[i]
      else: return False
    elif d[pattern[i]] != lst[i]:
      return False
  return True

