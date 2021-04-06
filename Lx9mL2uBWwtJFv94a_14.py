
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
  els = [el1, el2]
  board = []
  for i in range(n):
    row = []
    k = i
    for j in range(n):
      row.append(els[k%2])
      k += 1
    board.append(row)
  return board

