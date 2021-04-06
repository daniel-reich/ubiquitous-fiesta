
def is_mini_sudoku(square):
  new_list = []
  numbers=[1,2,3,4,5,6,7,8,9]
  for x in square:
    for y in x:
      new_list.append(y)
  new_list.sort()
  if new_list == numbers:
    return True
  else: return False

