
def is_undulating(n):
  if len(list(str(n))) < 3:
    return False
  if len(set(list(str(n)))) != 2:
    return False
  for i in range(len(list(str(n)))-1):
    if list(str(n))[i] == list(str(n))[i+1]:
      return False
  return True

