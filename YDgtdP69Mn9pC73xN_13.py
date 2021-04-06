
def num_grid(lst):
  result = [[i if i == "#" else 0 for i in row] for row in lst]
​
  for i, row in enumerate(lst):
    for j, item in enumerate(row):
      if item == "#":
        result = check_borders(result, i, j)
  return [[str(i) for i in row] for row in result]
​
def check_borders(lst, row, col):
  for i in range(-1, 2):
    for j in range(-1, 2):
      try:
        if lst[row + i][col + j] != "#" and row + i >= 0 and col + j >= 0:
          lst[row + i][col + j] = lst[row + i][col + j] + 1
      except IndexError:
        pass
        
  return lst

