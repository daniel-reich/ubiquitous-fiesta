
def diagonalize(n, d):
  board = [[i + j for j in range(n)] for i in range(n)]
​
  if d == 'ul':
    return board
  elif d == 'ur':
    return [row[::-1] for row in board]
  elif d == 'll':
    return board[::-1]
  else:
    return [row[::-1] for row in board][::-1]

