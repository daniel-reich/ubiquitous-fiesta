
def check_pattern(lst, pattern):
  return all([(lst[i] == lst[j]) == (pattern[i] == pattern[j]) for i in range(len(lst)) for j in range(i)])

