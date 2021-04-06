
def most_overlapped_block(grid_width, points):
  max_overlap = 0
  grid = {}
​
  for point in points:
    x, y, r = point
    col_blocks = 1
​
    for i in range(r * 2 + 1):
      for j in range(abs(col_blocks)):
        x2 = x - r + i
        y2 = y - j + abs(col_blocks) // 2
​
        if 0 < x2 <= grid_width and 0 < y2 <= grid_width:
          pos = (x2, y2)
​
          try:
            grid[pos] += 1
          except KeyError:
            grid[pos] = 1
​
          if grid[pos] > max_overlap:
            max_overlap = grid[pos]
​
      if (col_blocks / 2) > r:
        col_blocks *= -1
      col_blocks += 2
​
  return max_overlap

