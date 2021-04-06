
def x_and_o(board):
  available = []
  
  col1 = []
  col2 = []
  col3 = []
  left = []
  right = []
  
  plus_idx = 0
  minus_idx = 4
  for row in board:
    # adding rows
    available.append([row[0], row[2], row[4]])
    left.append(row[plus_idx])
    right.append(row[minus_idx])
    plus_idx += 2
    minus_idx -= 2
    
    # cols
    col1.append(row[0])
    col2.append(row[2])
    col3.append(row[4])
  
  # adding cols
  available.append(col1)
  available.append(col2)
  available.append(col3)
  
  # adding inclines
  available.append(left)
  available.append(right)
​
  win_condition = []
  for idxx, i in enumerate(available):
    if i.count("X") == 2 and i.count(" ") == 1:
      win_condition = [i, idxx]
​
  pos = []
  
  # unwinnable
  if win_condition == []:
    pos = False
​
  # winnable
  if win_condition != []:
    space_pos = win_condition[0].index(" ") + 1
    if win_condition[1] < 3:  # <- rows
      pos = [win_condition[1] + 1, space_pos]
    elif 2 < win_condition[1] < 6:  # <- cols
      pos = [space_pos, win_condition[1] + 1 - 3]
    elif win_condition[1] == 6:  # <- left
      pos = [space_pos, space_pos]
    elif win_condition[1] == 7:  # <- right
      blank_pos = 2
      if space_pos == 1:
        blank_pos = 3
      if space_pos == 3:
        blank_pos = 1
      pos = [space_pos, blank_pos]
  
  return pos

