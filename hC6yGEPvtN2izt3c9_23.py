
def is_mini_sudoku(square):
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for i in square:
    for x in i:
      if x in nums:
        nums.remove(x)
  if not nums:
    return True
  else:
    return False

