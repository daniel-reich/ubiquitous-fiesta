
def largest_island(lst):
  moves=[(1,0),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1),(1,1)]
  island, has_ones=0, False
  y=[i for i in range(len(lst))]
  x=[i for i in range(len(lst[0]))]
  for i in range (len(lst)):
    for j in range (len(lst[0])):
      if (lst[i][j]==1):
        has_ones=True
        for move in moves:
          if (i+move[0] in y and j+move[1] in x):
            if(lst[i+move[0]][j+move[1]]==1):
              island+=1
              break
  if has_ones:
    if island ==0:
      return 1
    else:
      return island
  else:
      return 0

