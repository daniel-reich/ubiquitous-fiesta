
def check_pattern(lst, pattern):
  for i in range (len(pattern)):
    for j in range (1,len(pattern)):
      if pattern[i]==pattern[j]:
        if lst[i]!=lst[j]:
          return False
      else:
        if lst[i]==lst[j]:
          return False
  return True

