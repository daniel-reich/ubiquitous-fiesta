
def is_there_consecutive(lst, n, times):
  for i in range(len(lst)-times):
    if all([lst[i+j]==n for j in range(times)]):
      return True
  return False

