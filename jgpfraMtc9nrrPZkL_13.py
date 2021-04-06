
def switch_gravity_on(lst):
  rows = len(lst)
  cols = len(lst[0])
  
  #get heights
  heights = [0 for _ in range(cols)]
  for i in range(rows):
    for j in range(cols):
      heights[j] += lst[i][j] == '#'
      
  #construct new lsts
  newlst = [['-' for __ in range(cols)] for _ in range(rows)]
  for j, h in enumerate(heights):
    for i in range(h):
      newlst[-i-1][j] = '#'
      
  return newlst

