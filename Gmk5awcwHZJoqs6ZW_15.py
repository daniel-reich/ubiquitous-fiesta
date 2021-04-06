
def largest_island(lst):
  def countisland(i,j):
    if touchedboard[i][j]: return 0
    touchedboard[i][j] = 1
    if resizedlst[i][j] == 0: return 0
    s = 1
    s += countisland(i-1, j-1)
    s += countisland(i-1, j+1)
    s += countisland(i-1, j)
    s += countisland(i, j-1)
    s += countisland(i, j+1)
    s += countisland(i+1, j-1)
    s += countisland(i+1, j+1)
    s += countisland(i+1, j)
    return s
​
  resizedlst, touchedboard = resize_and_copy(lst)
  highest = 0
​
  for i in range(1,len(lst)+1):
    for j in range(1,len(lst[0])+1):
      if resizedlst[i][j] and touchedboard[i][j] == 0:
        c = countisland(i,j)
        if c > highest:
          highest = c
      touchedboard[i][j] = 1
  return highest
  
  
def resize_and_copy(lst):
  h = len(lst)
  w = len(lst[0]) + 2
  touchedboard = []
  newlst = []
  newlst.append([0] * w)
  touchedboard.append([0] * w)
  for i in range(h):
    newlst.append([0] + lst[i] + [0])
    touchedboard.append([0] * w)
  touchedboard.append([0] * w)
  newlst.append([0] * w)
  return (newlst, touchedboard)

