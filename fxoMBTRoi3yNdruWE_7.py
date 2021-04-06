
def in_box(lst):
  l = len(lst)
  w = len(lst[0])
  print(l, w)
  for i in range(1,l-1):
    for j in range(1,w-1):
      if lst[i][j] == '*':
        return True
  return False

