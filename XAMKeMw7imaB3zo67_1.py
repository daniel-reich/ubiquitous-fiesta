
def trace_word_path(word, grid):
  lr = len(grid)
  lc = len(grid[0])
  for r in range(lr):
    for c in range(lc):
      if grid[r][c] == word[0]:
        coords = trace_word_recurse(word[1:], grid, r, c, [])
        if coords != None and coords[-1] != "Not present":
          return coords
  return "Not present"
​
def trace_word_recurse(word, grid, r, c, coords):
  lr = len(grid)-1
  lc = len(grid[0])-1
  if not word:
    return coords + [(r,c)]
  if r > 0:
    if grid[r-1][c] == word[0] and (r-1, c) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r-1, c, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  if r < lr:
    if grid[r+1][c] == word[0] and (r+1, c) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r+1, c, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  if c > 0:
    if grid[r][c-1] == word[0] and (r, c-1) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r, c-1, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  if c < lc:
    if grid[r][c+1] == word[0] and (r, c+1) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r, c+1, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  return coords + ["Not present"]

