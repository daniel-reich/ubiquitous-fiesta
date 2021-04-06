
def check_pattern(lst, pattern):
  for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
      if (lst[i] == lst[j]) != (pattern[i] == pattern[j]):
        return False
  return True

