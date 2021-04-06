
def get_path_length(world, width, height):
  world = [world.split(',')[row*width:(row+1)*width] for row in range(height)]
  step_count = [[0 for step in world] for row in world]
  if height == 1:
    return len(world[0]) - 1
    
  def start(li, li2):
    for i in range(len(li)):
      for j in range(len(li[i])):
        if li[i][j] == 'm':
          return [i,j]
​
  def end(li, li2):
    for i in range(len(li)):
      for j in range(len(li[i])):
        if li[i][j] == 'h':
          return [i,j]
  
  matt = start(world, step_count)
  house = end(world, step_count)
  count_of_zeros = 0
  
  def move(range1, range2):
    for i in range1:
      for j in range2:
        if world[row+i][col+j] == 't':
          continue
        elif step_count[row+i][col+j] != 0 and step_count[row+i][col+j] < step_count[row][col] + 1:
          continue
        else:
          step_count[row+i][col+j] = step_count[row][col] + 1
          
  while step_count[house[0]][house[1]] == 0:
    step_count[matt[0]][matt[1]] = 1
    zeros = []
    for row in range(len(world)):
      for col in range(len(world[0])):
        if step_count[row][col] == 0:
          zeros.append(step_count[row][col])
        elif row == 0 and col == 0:
          move((0,1), (0,1))
        elif row == 0 and col != len(world[0]) - 1:
          move((0,1), (-1,0,1))
        elif row == 0 and col == len(world[0]) - 1:
          move((0,1), (-1,0))
        elif row != 0 and row != len(world) - 1 and col == 0:
          move((-1,0,1), (0,1))
        elif row == len(world) - 1 and col == 0:
          move((-1,0), (0,1))
        elif row == len(world) - 1 and col != 0 and col != len(world[0]) - 1:
          move((-1,0), (-1,0,1))
        elif row == len(world) - 1 and col == len(world[0]) - 1:
          move((-1,0), (-1,0))
        elif row != len(world) - 1 and col == len(world[0]) - 1:
          move((-1,0,1), (-1,0))
        else:
          move((-1,0,1), (-1,0,1))
    if len(zeros) == count_of_zeros:
      break
    else:
      count_of_zeros = len(zeros)
  return step_count[house[0]][house[1]] -1

