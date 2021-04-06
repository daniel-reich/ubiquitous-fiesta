
def in_box(lst):
  for i in range(1,len(lst)):
    for j in range(1,len(lst[i])):
      if lst[i][j]=='*':
        return True
  return False

