
def largest_island(lst):
  directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  width = len(lst)
  height = len(lst[0])
  def contiguous_cells(x0,y0):
          if lst[x0][y0] == 1:
              lst[x0][y0] = 0
              adjacent = [(x0 + dx,y0 + dy) for (dx,dy) in directions if 0 <= x0+dx < width and 0 <= y0+dy < height]
              adjacent_ones = [(x,y) for (x,y) in adjacent if lst[x][y] == 1]
              island = [(x0,y0)]
              for cell in adjacent_ones:
                  island = island + contiguous_cells(*cell)
              return island
          return []
  max_size = 0
  for x,row in enumerate(lst):
      for y,cell in enumerate(row):
          if cell:
              max_size = max(max_size, len(contiguous_cells(x,y)))
  return max_size

