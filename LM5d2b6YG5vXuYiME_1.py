
def can_enter_cave(x):
  higth = len(x)
  width = len(x[0])
  i = 0
  j = 0
​
  # find start point
  while x[i][0] != 0:
    i += 1
​
  def check_vertically(x, start, stop, step, jj, horizontal_step):
    for ii in range(start, stop, step):
      if x[ii][jj]:
        return start, jj, False
      if x[ii][jj+horizontal_step] == 0:
        return ii, jj+horizontal_step, True
    return start, jj, False
​
  while j < width-1:
    # Check Down and Forward
    i, j, found_way = check_vertically(x, i, higth, 1, j, +1)
    if not found_way:
      # Check Up and Forward
      i, j, found_way = check_vertically(x, i - 1, -1, -1, j, +1)
    if not found_way:
      # Check Down and Backward
      i, j, found_way = check_vertically(x, i, higth, 1, j, -1)
    if not found_way:
      # Check Up and Backward
      i, j, found_way = check_vertically(x, i - 1, -1, -1, j, -1)
    if not found_way:
      return False
  return True

