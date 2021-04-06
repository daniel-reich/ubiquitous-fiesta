
def num_grid(lst):
  height = len(lst)
​
  width = len(lst[0])
​
  result = [["0" for i in range(width)] for j in range(height)]
​
  mines = []
​
  for i in range(height):
    for j in range(width):
      if lst[i][j] == "#":
        mines.append([i, j])
​
  for i in mines:
    result[i[0]][i[1]] = "#"
​
  for i in mines:
    x, y = i
    for j in [-1, 0, 1]:
      for k in [-1, 0, 1]:
        try:
          if (j == -1 and x > 0) or (j == 1 and x < height - 1) or j == 0:
            if (k == -1 and y > 0) or (k == 1 and y < width - 1) or k == 0:
              if result[x + j][y + k] != "#":
                  result[x + j][y + k] = str(int(result[x + j][y + k]) + 1)
        except:
          pass
​
  return result
​
  for i in mines:
    x, y = i
    for j in [-1, 0, 1]:
      for k in [-1, 0, 1]:
        try:
          if result[x + j][y + k] != "#":
            result[x + j][y + k] = str(int(result[x + j][y + k]) + 1)
        except:
          pass
​
  return result

