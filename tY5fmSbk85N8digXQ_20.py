
def ones_infection(arr):
  nRows = len(arr)
  nCols = len(arr[0])
  outrow = []
  outcol = []
  for row in range(nRows):
    for col in range(nCols):
      if arr[row][col] == 1:
        outrow.append(row)
        outcol.append(col)
  for row in range(nRows):
    if row in outrow:
      arr[row] = [1]*nCols
    else:
      arr[row] = [0]*nCols
      for col in range(nCols):
        if col in outcol:
          arr[row][col] = 1
  return arr

