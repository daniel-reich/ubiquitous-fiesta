
def can_enter_cave(x):
  for column in range(len(x[0])-1):
    for row in range(len(x)):
      if x[row][column] == 0 and x[row][column+1] == 0:
        break
      if row == (len(x)-1): return False
  return True

