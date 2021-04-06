
def game_of_life(board):
  ans=""
  neigh=neighbours(board)
  for y in range(len(board)):
    for x in range(len(board[0])):
      if board[y][x]==0:
        if neigh[y][x]==3:
          ans+="I"
        else:
          ans+="_"
      else:
        if neigh[y][x]<=1 or neigh[y][x]>=4:
          ans+="_"
        elif neigh[y][x]==2 or neigh[y][x]==3:
          ans+="I"
    ans+="\n"
  return ans[:-1]
​
​
def neighbours(board):
  empty=[[0 for i in range(len(board[0]))] for i in range(len(board))]
  for x in range(len(board[0])):
    for y in range(len(board)):
      if board[y][x]==1:
        for coord in [[y,x-1],[y,x+1],[y-1,x],[y+1,x],[y-1,x-1],[y+1,x+1],[y-1,x+1],[y+1,x-1]]:
          if len(board)-1>=coord[0]>=0 and len(board[0])-1>=coord[1]>=0:
            empty[int(coord[0])][int(coord[1])]+=1
  return empty

