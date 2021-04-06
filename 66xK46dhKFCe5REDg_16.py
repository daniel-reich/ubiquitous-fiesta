
def x_and_o(board):
  def board_to_list(bo = board):
    e = [] #The 1 dimensional list that will house the other lists
    for a in range(3): #Just puts the board into a 2 dimensional lst
      l = board[a].split("|")
      e.append(l)
    return e
  def win(lst): #This function determines if a board is a win for X
    if lst[0][0] == 'X' and lst[1][0] == 'X' and lst[2][0] == 'X':
      return True
    if lst[0][1] == 'X' and lst[1][1] == 'X' and lst[2][1] == 'X':
      return True 
    if lst[0][2] == 'X' and lst[1][2] == 'X' and lst[2][2] == 'X':
      return True
    if lst[0][0] == 'X' and lst[0][1] == 'X' and lst[0][2] == 'X':
      return True
    if lst[1][0] == 'X' and lst[1][1] == 'X' and lst[1][2] == 'X':
      return True
    if lst[2][0] == 'X' and lst[2][1] == 'X' and lst[2][2] == 'X':
      return True
    if lst[0][0] == 'X' and lst[1][1] == 'X' and lst[2][2] == 'X':
      return True
    if lst[0][2] == 'X' and lst[1][1] == 'X' and lst[2][0] == 'X':
      return True
    else:
      return False
  w = []
  f = board_to_list()
  for a in range(3): #row
    for b in range(3): #column
      g = f[a][b] #This allows the board position to be restored to before the attempt
      f[a][b] = 'X' if f[a][b] != 'O' else ''
      if win(f): #If it results in a win, it will return that
        return [a+1,b+1]
      else:
        f[a][b] = g
  if w == []:
    return False

