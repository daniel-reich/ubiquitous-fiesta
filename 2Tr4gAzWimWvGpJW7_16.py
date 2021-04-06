
def is_there_consecutive(lst, n, times):
  if times == 0:
    return False if n in lst else True
  cnt = 0
  for i in lst:
    if i == n:
      cnt += 1
      if cnt == times:
        return True
    else:
      cnt = 0
  return False

