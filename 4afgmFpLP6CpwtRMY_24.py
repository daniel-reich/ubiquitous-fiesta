
def sudoku_validator(grid):
  req     = {i for i in range(1, 10)}
  rows    = [set() for i in range(9)]
  columns = [set() for i in range(9)]
  squares = [[set() for i in range(3)] for j in range(3)]
​
  for row_num, row in enumerate(grid):
    for column_num, value in enumerate(row):
      squares[column_num // 3][row_num // 3].add(value)
      columns[row_num].add(value)
      rows[column_num].add(value)
​
  for test in columns + rows + squares[0] + squares[1] + squares[2]:
    if test != req:
      return False
  return True

