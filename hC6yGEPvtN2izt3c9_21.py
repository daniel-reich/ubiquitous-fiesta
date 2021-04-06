
def is_mini_sudoku(square):
  a = '123456789'
  lst = []
  for i in square:
    for j in i:
      if str(j) in a:
        lst.append(j)
      else:
        return False
  if len(set(lst)) < len(lst):
    return False
  return True

