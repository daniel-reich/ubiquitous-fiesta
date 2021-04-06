
def largest_island(lst):
  alreadyPassed = [[0 for i in range(len(lst[0]))] for j in range(len(lst))]
  maxArea = 0
  INCREMENT = 0
  RESET = 1
  GET_VAR = 2
  
  def staticVarManagement(action):
    if action == RESET:
      staticVarManagement.counter = 0
    elif action == INCREMENT:
      staticVarManagement.counter += 1
    return staticVarManagement.counter
  
  def computeArea(x,y):
    if x >= 0 and x < len(lst) and y >= 0 and y < len(lst[0]):
      if alreadyPassed[x][y] == 0 and lst[x][y] == 1:
        staticVarManagement(INCREMENT)
        alreadyPassed[x][y] = 1
        for dx in range(-1,2):
          for dy in range(-1,2):
            computeArea(x+dx,y+dy)
  
  for x,subLst in enumerate(lst):
    for y,elmt in enumerate(subLst):
      staticVarManagement(RESET)
      computeArea(x,y)
      maxArea = max(maxArea,staticVarManagement(GET_VAR))
  return maxArea

