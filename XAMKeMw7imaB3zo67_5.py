
def trace_word_path(word, grid):
  x, y = len(grid), len(grid[0])
  target = len(word)
​
  for row in range(x):
    for col in range(y):
      if grid[row][col] == word[0]:
        indices = get_index(word, word[1:], grid, x, y, row, col, [(row, col)], target)
        if len(indices) == target:
          return indices
  return 'Not present'
​
def get_index(word, start, grid, x, y, row, col, indices, target):
  if len(indices) == target:
    return indices
  moves = [(1,0),(0,1),(-1,0),(0,-1)]
  neighbors = [(row+i,col+j) for i, j in moves if 0 <= row+i < x and 0 <= col+j < y]
  neighbors = [(i,j) for i,j in neighbors if grid[i][j] == start[0]]
  for a, b in neighbors:
    if (a, b) not in indices:
      n_indices = indices + [(a, b)]
      if len(n_indices) == target:
        return n_indices
      indices_r = get_index(word, start[1:], grid, x, y, a, b, n_indices, target)
      if len(indices_r) == target:
        return indices_r
  return indices

