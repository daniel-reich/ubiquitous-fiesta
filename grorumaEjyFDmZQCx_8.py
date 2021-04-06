
def is_wristband(lst):
  a = check_horizontal(lst)
  b = check_vertical(lst)
  c = check_left_diagonal(lst)
  d = check_right_diagonal(lst)
​
  if (a+b+c+d>0):
    return True
  else:
    return False
  
def check_horizontal(lst):
  for i in range(0,len(lst)):
    for j in range(0,len(lst[i])-1):
      if(lst[i][j] != lst[i][j+1]):
        return 0
  return 1
  
def check_vertical(lst):
  for i in range(0,len(lst[0])):
    for j in range(0,len(lst)-1):
      if(lst[j][i] != lst[j+1][i]):
        return 0
  return 1
​
def check_left_diagonal(lst):
  for i in range(0,len(lst)-1):
    for j in range(0,len(lst[0])-1):
      if(lst[i][j] != lst[i+1][j+1]):
        return 0
  return 1
    
def check_right_diagonal(lst):
  for i in range(0,len(lst)-1):
    for j in range(0,len(lst[0])-1):
      if(lst[len(lst)-i-1][j] != lst[len(lst)-i-2][j+1]):       
        return 0
  return 1

