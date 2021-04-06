
def can_patch(bridge, planks):
  holes = []
  boards = planks
  counter = -1
  while counter < len(bridge) - 1:
    counter += 1
    if bridge[counter] == 0:
      var = counter
      while bridge[counter] == 0:
        counter += 1
      holes.append(bridge[var:counter])
  for hole in holes:
    if len(hole) == 1:
      continue
    if boards == []:
      return False
    for x in range(len(boards)):
      if boards[x] == len(hole) or boards[x] == len(hole) - 1:
        boards.pop(x)
        break
      if x == len(boards) - 1:
        return False
  return True

