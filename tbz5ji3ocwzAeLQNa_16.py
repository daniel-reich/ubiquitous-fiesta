
import numpy 
​
def exit_maze(maze, directions):
​
  #find starting position, assuming it is unique
  maze_arr=numpy.array(maze)
  r,c=numpy.where(maze_arr==2)
  row_start=numpy.asscalar(r)
  col_start=numpy.asscalar(c)
  row_start=9
  col_start=8
​
  for i in range(len(directions)):
    d = directions[i]
    
    if (d=="N"):
      row_start-=1
      if (row_start>9 or row_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
​
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"
​
​
    if (d=="S"):
      row_start+=1
      
      if (row_start>9 or row_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"
​
​
    if (d=="E"):
      col_start+=1
      
      if (col_start>9 or col_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
      
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"
​
​
    if (d=="W"):
      col_start-=1
      if (col_start>9 or col_start<0):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==1):
        return "Dead"
        
      elif (maze_arr[row_start][col_start]==3):
        return "Finish"
        
      elif (maze_arr[row_start][col_start]==0 and i==(len(directions)-1)):
        return "Lost"
​
      elif (maze_arr[row_start][col_start]==2 and i==(len(directions)-1)):
        return "Lost"

