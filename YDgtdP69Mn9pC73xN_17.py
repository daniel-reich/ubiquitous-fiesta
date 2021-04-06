
def add(num):
  if num != "#":
    num += 1
  return num
​
def num_grid(lst):
  for row in range(5):
    for column in range(5):
      if lst[row][column] == "-":
        lst[row][column]=0
  for row in range(5):
    for column in range(5):
      if lst[row][column]=="#":
        if row != 4:
          if column != 4:
            lst[row+1][column+1] = add(lst[row+1][column+1])
          lst[row+1][column] = add(lst[row+1][column])
          if column != 0:
            lst[row+1][column-1] = add(lst[row+1][column-1])
        if column != 4:
          lst[row][column+1] = add(lst[row][column+1])
        if column != 0:
          lst[row][column-1] = add(lst[row][column-1])
        if row != 0:
          if column != 4:
            lst[row-1][column+1] = add(lst[row-1][column+1])
          lst[row-1][column] = add(lst[row-1][column])
          if column != 0:
            lst[row-1][column-1] = add(lst[row-1][column-1])
        print(lst)
  for row in range(5):
    for column in range(5):
      lst[row][column] = str(lst[row][column])
  return lst

