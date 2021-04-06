
def sudoku_validator(solution):
  valid = True
  # Validate squares
  for square in sudoku_get_squares(solution):
    if (not sudoku_group_valid(square)):
      valid = False
​
  # Validate the columns
  for column in sudoku_get_columns(solution):
    if (not sudoku_group_valid(column)):
      valid = False
​
  # Validate the rows
  for row in solution:
    if (not sudoku_group_valid(row)):
      valid = False
​
  return valid
​
def sudoku_group_valid(group):
  valid = True
  # Check the 1 - 9 values are unique
  for num in range(1, 10):
    if (group.count(num) > 1):
      valid = False
  return valid
​
def sudoku_get_columns(solution):
  columns = []
  for x in range(0, 9):
    column = []
    for y in range(0, 9):
      column.append(solution[y][x])
    columns.append(column)
  return columns
​
def sudoku_get_squares(solution):
  squares = []
  # Looking at the center item of each square and
  # pulling the square based on that
  for y in range(1, 8, 3):
    for x in range(1, 8, 3):
      square = []
      square.extend(solution[y - 1][x - 1 : x + 2])
      square.extend(solution[y]    [x - 1 : x + 2])
      square.extend(solution[y + 1][x - 1 : x + 2])
      squares.append(square)
  return squares

