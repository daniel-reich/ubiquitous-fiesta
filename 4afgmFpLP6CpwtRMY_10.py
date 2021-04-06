
def sudoku_validator(array):
  formula = [i for i in range(1, 10)]
  squares = [[], [], []]
  for idx, row in enumerate(array):
    if sorted(row) != formula:
      return False
    fullcol = []
    for col in range(9):
      fullcol.append(array[col][idx])
    if sorted(fullcol) != formula:
      return False
    for plus in range(3):
      squares[0].append(row[0 + plus])
      squares[1].append(row[3 + plus])
      squares[2].append(row[6 + plus])
    if idx in [2, 5, 8]:
      for square in squares:
        if sorted(square) != formula:
          return False
      squares = [[], [], []]
  return True

