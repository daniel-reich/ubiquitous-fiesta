
def who_won(board):
  row = [i[0] for i in board if len(set(i))==1]
  col = [k[0] for k in [[i[j] for i in board] for j in range(3)] if len(set(k))==1]
  dia1 = [board[0][0]] if len(set([board[i][i] for i in range(3)]))==1 else []
  dia2 = [board[1][1]] if len(set([board[i][2-i] for i in range(3)]))==1 else []
  s = row + col + dia1 + dia2
  return s[0]

