
def in_box(lst):
  for i in range(1,len(lst)-1):
    for j in range(1,len(lst[i])-1):
      if lst[i][j] == '*':
        return True
  return False

