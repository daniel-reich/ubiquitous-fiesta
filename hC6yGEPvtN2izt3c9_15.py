
def is_mini_sudoku(square):
  FlatArray1 = []
  FlatArray2 = []
  for lvl1 in range(len(square)):
    for lvl2 in range(len(square[lvl1])):
      if square[lvl1][lvl2] > 0:
        FlatArray1.append(square[lvl1][lvl2])
      FlatArray2.append(square[lvl1][lvl2])
  return len(FlatArray1) == len(set(FlatArray2))

