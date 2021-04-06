
def minesweeper_numbers(board):
  height = len(board)
​
  for y in range(height):
      for x in range(height):
          el = board[y][x]
          if el==1:
              board[y][x]=9
​
  for y in range(height):
      for x in range(height):
          el = board[y][x]
          if el!=9:
              if x>0:
                  if board[y][x-1]==9:     #check left
                      board[y][x]+=1     
              if x<height-1:
                  if board[y][x+1]==9:     #check right
                      board[y][x]+=1   
              if y>0:
                  if board[y-1][x]==9:     #check up
                      board[y][x]+=1     
              if y<height-1:
                  if board[y+1][x]==9:     #check down
                      board[y][x]+=1
              if x>0 and y>0:
                  if board[y-1][x-1]==9:   #check north-west
                      board[y][x]+=1
              if x<height-1 and y>0:
                  if board[y-1][x+1]==9:   #check north-east
                      board[y][x]+=1
              if x>0 and y<height-1:
                  if board[y+1][x-1]==9:   #check south-west
                      board[y][x]+=1
              if x<height-1 and y<height-1:
                  if board[y+1][x+1]==9:   #check south-west
                      board[y][x]+=1
  return board

