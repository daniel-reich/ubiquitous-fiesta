
def is_mini_sudoku(square):
  nums = ''
  for i in range(3):
    for j in range(3):
      if str(square[i][j]) not in nums:
        nums+=str(square[i][j])
  return ''.join(sorted(nums))=='123456789'

