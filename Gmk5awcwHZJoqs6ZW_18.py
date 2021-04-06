
def largest_island(lst):
  rows = len(lst)
  columns = len(lst[0])
  output = []
  numberOfIslands = countIslands(rows,columns,lst,output)
  return max(output)
​
def isValid(r,c,rows,columns,visited,lst):
  if (r >= 0 and c >= 0 and r < rows and c < columns):
    return (not visited[r][c] and lst[r][c] == 1)
​
def DFS(r,c,rows,columns,visited,lst,output,islandLength):
  rowNumbers = [-1,-1,-1,0,0,1,1,1]
  columnNumbers = [-1,0,1,-1,1,-1,0,1]
  visited[r][c] = True
  for i in range(8):
    if (isValid(r + rowNumbers[i], c + columnNumbers[i], rows, columns, visited, lst)):
      islandLength = islandLength + 1
      DFS(r + rowNumbers[i], c + columnNumbers[i], rows, columns, visited,lst,output,islandLength)
  
  output.append(islandLength)
​
def countIslands(rows,columns,lst,output):
  visited = [[False for r in range(columns)]for c in range(rows)]
  count = 0
  for r in range(rows):
    for c in range(columns):
      islandLength = 0
      if visited[r][c] == False and lst[r][c] == 1:
        islandLength = islandLength + 1
        DFS(r,c,rows,columns,visited,lst,output,islandLength)
        count = count + 1
  return count

