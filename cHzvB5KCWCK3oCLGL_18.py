
def game_of_life(board):
  h, w = len(board), len(board[0])
  bounded_get = lambda i, j: board[i][j] if (i >= 0 and i < h and j >= 0 and j < w) else 0
  def count_neighbors(i, j):
    return sum([bounded_get(i - 1 + (k // 3), j - 1 + (k % 3)) for k in range(9)]) - board[i][j]
  
  out = []
  for i in range(h):
    out.append([])
    for j  in range(w):
      n = count_neighbors(i, j)
      oc = '_'
      if board[i][j]:
        if n == 2 or n == 3:
          oc = 'I'
      elif n == 3:
          oc = 'I'
      out[i].append(oc)
  return '\n'.join([''.join(row) for row in out])

