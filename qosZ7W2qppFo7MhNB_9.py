
def hex_distance(grid):
  lst1,row,col=[],[],[]
  for i in range (len(grid)):
    lst=[0 if v == 'o' else 1 if v == 'x' else 'blank' for v in grid[i]]
    lst = list(filter(lambda x: x!= "blank", lst))
    lst1.append(lst)
  for i in range (len (lst1)):
    for j in range (len(lst1[i])):
      if (lst1[i][j]==1):
        row.append(i)
        col.append(j)
  if (row[0]==row[1]):
    return(abs(col[0]-col[1]))
  else:
    curr_row,curr_col,steps=row[1],col[1],0
    if (row[0] >= int(len(lst1)/2) and row[1] >= int(len(lst1)/2)):
      while not (curr_row==row[0]):
        if (col[0]<=col[1]):
          curr_row -=1
          steps+=1
        else:
          curr_row-=1
          steps+=1
          curr_col +=1
      return (abs(col[0]-curr_col)+steps)
    elif(row[0] < int(len(lst1)/2) and row[1] <= int(len(lst1)/2)):
      while not (curr_row==row[0]):
        if (col[0]<=curr_col):
          curr_row -=1
          if (curr_col>col[0]):
            curr_col -=1
          steps+=1
        else:
          curr_row-=1
          steps+=1
      return (abs(col[0]-curr_col)+steps)
    elif(row[0] < int(len(lst1)/2) and row[1] > int(len(lst1)/2)):
      while not (curr_row==row[0]):
        if (col[0]<=curr_col and curr_row > int(len(lst1)/2)):
          curr_row-=1
          steps+=1
        elif (col[0]<=curr_col and curr_row <= int(len(lst1)/2)):
          if (curr_col > col[0]):
            curr_col-=1
          curr_row-=1
          steps+=1
        elif(curr_col<col[0] and curr_row >= int(len(lst1)/2)):
          curr_col+=1
          curr_row-=1
          steps+=1
        elif(curr_col<col[0] and curr_row < int(len(lst1)/2)):
          curr_row-=1
          steps+=1
      return (abs(col[0]-curr_col)+steps)

