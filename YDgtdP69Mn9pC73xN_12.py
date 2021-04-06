
def num_grid(lst):
  
  copy = []
  for i in range(len(lst)):
    copy.append(lst[i])
​
  for y in range(len(lst)):
    for x in range(len(lst[y])):
      if lst[y][x] == '-':
        numMines = 0
        for dy in range(y - 1, y + 2):
          for dx in range(x - 1, x + 2):
            bound = dy >= 0 and dy < len(lst) and dx >= 0 and dx < len(lst[y])
            same = dy == y and dx == x
            if bound and not same and copy[dy][dx] == '#':
              numMines += 1
        lst[y][x] = str(numMines)
  
  return lst

