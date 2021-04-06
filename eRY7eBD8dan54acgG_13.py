
def is_checkerboard(lst):
  for st in lst:
    for i in range(len(lst)-1):
      if st[i]==st[i+1]:
        return False
  return True

