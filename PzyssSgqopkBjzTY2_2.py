
def move(cord,shift):
  x=cord[0]+shift[0]
  y=cord[1]+shift[1]
  return (x,y)
​
def can_exit(lst):
  cordinates = {}
  for y in range(0,len(lst)):
    for x in range(0,len(lst[y])):
      cordinates[(x,y)] = bool(lst[y][x]-1)
  goal = (x,y)
      
  directions = [(-1,0),(1,0),(0,-1),(0,1)]
  position = (0,0)
  walked_cords = []
  save_points = []
​
  while True:
    options = []
    for movement in directions:
      try:
        if cordinates[move(position,movement)] == True and move(position,movement) not in walked_cords:
          options.append(move(position,movement))
      except:
        pass
    if goal in options:
      return True
    elif len(options) == 1:
      walked_cords.append(position)
      position = options[0]
    elif len(options) == 0 and save_points == []:
      return False
    elif len(options) == 0:
      position = save_points[-1]
      save_points.remove(position)
    else:
      walked_cords.append(position)
      position = options[0]
      for other_cords in options:
        save_points.append(other_cords)
      save_points.remove(position)
      save_points = list(set(save_points))

