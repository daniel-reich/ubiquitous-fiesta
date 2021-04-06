
def is_checkerboard(lst):
  x = lst[0][0]
  for row in range(len(lst)):
    for col in range(len(lst[0])):
      if lst[row][col] != (row + col + x)%2:
        return False
  return True

