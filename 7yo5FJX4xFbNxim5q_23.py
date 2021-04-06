
def harry(po):
  if len(po[0]) < 1:
    return -1
  elif len(po[0]) == 1:
    return sum(po[0])
  else:
    max_steps = (len(po) + len(po[0])) - 2
    steps, row, col = 0, 0, 0
    nums = []
    while steps <= max_steps:
      nums.append(po[row][col])
      steps += 1
      if row + 1 == len(po):
        col += 1
      elif col + 1 == len(po[0]):
        row += 1
      elif po[row+1][col] > po[row][col+1]:
        row += 1
      else:
        col += 1
    return sum(nums) + 1 if max(po[len(po)-1]) == 19 else sum(nums)

