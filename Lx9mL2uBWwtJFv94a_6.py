
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
  board = []
  rows = 0
  rowNum = 0
  while rowNum < n:
    curRow = []
    els = [el1, el2]
    if rowNum % 2 == 0:
      for i in range(0,n):
        curRow.append(els[i % 2])
    else:
      for i in range(1, n+1):
        curRow.append(els[i % 2])
    rowNum += 1
    board.append(curRow)
  return board

