
# 1-> find if cube is full or not, by checking len of cube vs len of current row.
​
# 2-> calculate the missing parts in current row, by deducting the longest len of row vs current row.
​
# 3-> if we have missing parts return it.
​
# 4-> if we don't have missing parts, but our len of cube is smaller than our longest row. then that means we have a non-full cube.
​
def identify(*cube):
  totalMissingParts = 0
  for row in range(len(cube)):
    maxLengthOfaRow = len(max([i for i in cube]))
    # Non-Full is True
    if len(cube) < maxLengthOfaRow or len(cube[row]) < maxLengthOfaRow:
      currentMissingParts = maxLengthOfaRow - len(cube[row])
      totalMissingParts += currentMissingParts
  
  if totalMissingParts:
    return "Missing {}".format(totalMissingParts)
  
  else:
    if len(cube) < maxLengthOfaRow and not totalMissingParts:
      return "Non-Full"
    else:
      return "Full"

