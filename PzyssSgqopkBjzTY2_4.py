
def can_exit(lst):
  m = len(lst)
  n = len(lst[0])
  if lst[0][0] != 0 or lst[m-1][n-1] != 0:
    return False
  else:
    coord = (0,0)
    saveCoords = []
    while coord != (n-1, m-1):
      x = coord[0]
      y = coord[1]
      lst[y][x] = 7
      option, newCoords = find_options(lst, coord)
      if option == 0:
        if saveCoords == []:
          return False
        else:
          coord = saveCoords[0]
          saveCoords = saveCoords[1:]
      if option == 1:
        coord = newCoords[0]
      if option > 1:
        saveCoords.append((x, y) * (option-1))
        coord = newCoords[0]
    return True
​
​
def find_options(lst, coord):
  x = coord[0]
  y = coord[1]
  option = 0
  
  newCoords = []
  
  if x+1 < len(lst[0]):
    if lst[y][x+1] == 0:
      option += 1
      newCoords.append((x+1, y))
  if y+1 < len(lst):
    if lst[y+1][x] == 0:
      option += 1
      newCoords.append((x, y+1))
  if y-1 >= 0:
    if lst[y-1][x] == 0:
      option += 1
      newCoords.append((x, y-1))
  if x-1 >= 0:
    if lst[y][x-1] == 0:
      option += 1
      newCoords.append((x-1, y))
  
  return option, newCoords

