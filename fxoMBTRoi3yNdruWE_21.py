
def in_box(lst):
  for i in range(1, len(lst) - 1):
    if '*' in lst[i][1:-1]: return True
  return False

