
def is_mini_sudoku(square):
  lst = []
  for ar in square:
    lst.extend(ar)
  if 0 in lst:
    return False
  return len(set(lst)) == 9

