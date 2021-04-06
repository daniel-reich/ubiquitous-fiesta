
def num_regions(grid: list) -> int:
  ones = set((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])
  result = 0
  while len(ones) > 0:
    region = set([ones.pop()])
    while len(region) > 0:
      new_region = set()
      for a, b in region:
        for coords in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)):
          if coords in ones:
            new_region.add(coords)
            ones.remove(coords)
      region = new_region
    result += 1
  return result

