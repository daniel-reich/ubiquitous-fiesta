
def islands_perimeter(grid):
  return sum(sum((a+b)%2 for a,b in zip(row,row[1:])) for row in grid) + \
         sum(sum((a+b)%2 for a,b in zip(col,col[1:])) for col in zip(*grid)) +\
         sum(grid[0]) + sum(grid[-1]) + \
         sum(row[0] for row in grid) + sum(row[-1] for row in grid)

