
def is_mini_sudoku(square):
  summary = 0
  for i in range(len(square)):
    summary += sum(square[i])
  return summary == 45

