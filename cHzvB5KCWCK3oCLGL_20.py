
def game_of_life(board):
  new_board = [[0] *len(board[0]) for i in range(len(board))]
  for row in range(len(board)):
    for col in range(len(board[row])):
      neighbors = 0
      if row-1 >= 0:
        neighbors += sum(board[row-1][max(0, col-1):min(col+2, len(board[0]))])
      if row+1 <= len(board)-1:
        neighbors += sum(board[row+1][max(0, col-1):min(col+2, len(board[0]))])
      if col-1 >= 0:
        neighbors+= board[row][col-1]
      if col+1 <= len(board[0])-1:
        neighbors+= board[row][col+1]
      if (board[row][col] == 0 and neighbors == 3) or (board[row][col] == 1 and (neighbors == 2 or neighbors == 3)):
        new_board[row][col] = 1
  return '\n'.join([ ''.join(["I" if num == 1 else "_" for num in row]) for row in new_board])

