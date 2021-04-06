
def game_of_life(board):
  nb = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
  nbc=lambda x, y: sum(board[x+i][y+j] for i, j in nb if 0<=x+i<len(board) and 0<=y+j<len(board[0]))
  
  return '\n'.join(''.join(['_', 'I'][3 in (nbc(i,j), nbc(i,j)+c)] for j, c in enumerate(r)) for i, r in enumerate(board))

