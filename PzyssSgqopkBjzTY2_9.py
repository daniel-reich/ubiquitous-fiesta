
def Inpath(path,i,j):
  for pt in path:
    if pt == (i,j):
      return True
  path.append((i,j))
  return False
​
def getNext(path,lst,i,j):
  #move right,down,up ,left (i,j) = (x,y)
  #m,n = maxX,MaxY
  m = len(lst) - 1
  n = len(lst[0]) - 1 
  exitPt = (m,n)
  if exitPt == (i,j):
    return True
  
  returnBool =  False
  if (m >= i+1) and lst[i+1][j] == 0 and not Inpath(path,i+1,j):
    returnBool = returnBool or getNext(path,lst,i+1,j)
  
  if (n >= j+1) and lst[i][j+1] == 0 and not Inpath(path,i,j+1):
    returnBool = returnBool or getNext(path,lst,i,j+1)
  
  if (j-1 >= 0) and lst[i][j-1] == 0 and not Inpath(path,i,j-1):
    returnBool = returnBool or  getNext(path,lst,i,j-1)
  
  if (i-1 >= 0) and lst[i-1][j] == 0 and not Inpath(path,i-1,j):
    returnBool = returnBool or getNext(path,lst,i-1,j)
  
  return returnBool
​
def can_exit(lst):
  path = []
  path.append((0,0))
  return getNext(path,lst,0,0)

