
def checker_board(n, el1, el2):
  board =[]
  if el1 == el2:
    return ('invalid')
  for row in range(n):
    board.append([])
    for number in range(n):
      if row % 2 == 0:
        if number % 2 == 0:
          board[row].append(el1)
        else:
          board[row].append(el2)        
      else:
        if number % 2 == 0:
          board[row].append(el2)
        else:
          board[row].append(el1)
  return board

