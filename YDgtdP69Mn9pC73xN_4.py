
def num_grid(lst):
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j] != "#":
        lst[i][j] = "0"
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j] == "#":
        for x in range(-1,2):
          for y in range(-1,2):
            if i + x >= 0 and j + y >= 0 and i + x < len(lst) and j + y < len(lst[i]):
              if lst[i + x][j + y] != "#":
                lst[i + x][j + y] = str(int(lst[i + x][j + y]) + 1)
  return lst

