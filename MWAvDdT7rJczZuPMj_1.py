
def count_word(grid, word):
  n, m = len(grid), len(grid[0])
  l = len(word)
  dirs = {(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)}
  ans = 0
  for i in range(n):
    for j in range(m):
      for (r,s) in dirs:
        gr_w = "".join(grid[i+r*d][j+s*d] for d in range(l) \
                if i+r*d in range(n) and j+s*d in range(m)).upper()
        if gr_w == word.upper():
          for d in range(l):
            grid[i+r*d][j+s*d] = grid[i+r*d][j+s*d].lower()
          ans += 1
  return ans, grid

