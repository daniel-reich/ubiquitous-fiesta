
def bingo_check(board):
  l=board
  def check_horz(l):
    for i in range(len(l)):
          if (len(set(l[i])))==1:
             return True
             break
    else:
        return False
  def check_colm(l):
    for i in range(len(l)):
      c=[]
      for j in range(len(l)):
        c.append(l[j][i])
      if (len(set(c)))==1:
             return True
             break
    else:
        return False        
  def check_diag1(l):
    c=[]
    for i in range(len(l)):
      for j in range(len(l)):
        if i==j:
          c.append(l[i][j])
    if (len(set(c)))==1:
             return True
    else:
        return False 
  def check_diag2(l):
    c=[]
    for i in range(len(l)):
      for j in range(len(l)):
        if i==j:
          c.append(l[i][4-i])
    if (len(set(c)))==1:
             return True
    else:
        return False 
  return  check_horz(l) or check_colm(l) or check_diag2(l) or check_diag1(l)

