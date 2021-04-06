
def all_explode(grid):
  bomb_directions = {
    '+': [
      (-1, 0),
      (1, 0),
      (0, 1),
      (0, -1)
    ],
    'x': [
      (-1, -1),
      (-1, 1),
      (1, -1),
      (1, 1)
    ],
    '0': []
  }
  grid_width, grid_height = len(grid[0]), len(grid)
  
  explode_queue = [(0, 0)]
  while explode_queue:
    exploded_bomb = explode_queue.pop(0)
    row, column = exploded_bomb
    bomb_kind = grid[row][column]
    grid[row][column] = '0'
    for direction in bomb_directions[bomb_kind]:
      row_change, column_change = direction
      new_row = row + row_change
      new_column = column + column_change
      if 0 <= new_row < grid_height and 0 <= new_column < grid_width:
        explode_queue.append((new_row, new_column))
​
  all_exploded = len([elem
    for subgrid in grid
    for elem in subgrid
    if elem in ['+', 'x']
  ]) == 0
  return all_exploded

