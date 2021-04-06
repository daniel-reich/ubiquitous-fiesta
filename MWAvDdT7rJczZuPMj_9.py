
def count_word(grid, word):
  count = 0
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      temp = checkLeft(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[x][i] = grid[x][i].lower()
      temp = checkRight(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[x][i] = grid[x][i].lower()
      temp = checkUp(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i][y] = grid[i][y].lower()
      temp = checkDown(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i][y] = grid[i][y].lower()
      temp = checkDiagLeftUp(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
      temp = checkDiagLeftDown(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
      temp = checkDiagRightUp(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
      temp = checkDiagRightDown(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
  return (count,grid)
    
def checkLeft(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if y-i<0 or grid[x][y-i].upper()!=word[i]:
      return False
    else:
      ret.append(y-i)
  return ret
  
def checkRight(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if y+i>=len(grid[x]) or grid[x][y+i].upper()!=word[i]:
      return False
    else:
      ret.append(y+i)
  return ret
  
def checkUp(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x-i<0 or grid[x-i][y].upper()!=word[i]:
      return False
    else:
      ret.append(x-i)
  return ret
  
def checkDown(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x+i>=len(grid) or grid[x+i][y].upper()!=word[i]:
      return False
    else:
      ret.append(x+i)
  return ret
  
def checkDiagLeftUp(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x-i<0 or y-i<0 or grid[x-i][y-i].upper()!=word[i]:
      return False
    else:
      ret.append([x-i,y-i])
  return ret
  
def checkDiagLeftDown(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x+i>=len(grid) or y-i<0 or grid[x+i][y-i].upper()!=word[i]:
      return False
    else:
      ret.append([x+i,y-i])
  return ret
  
def checkDiagRightUp(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x-i<0 or y+i>=len(grid[x]) or grid[x-i][y+i].upper()!=word[i]:
      return False
    else:
      ret.append([x-i,y+i])
  return ret
  
def checkDiagRightDown(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x+i>=len(grid) or y+i>=len(grid[x]) or grid[x+i][y+i].upper()!=word[i]:
      return False
    else:
      ret.append([x+i,y+i])
  return ret

