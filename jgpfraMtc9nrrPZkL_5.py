
def switch_gravity_on(lst):
  block = "#"
  empty = "-"
​
  maxyIndex = len(lst) - 1
  maxxIndex = len(lst[0]) - 1
  
  for iteration in range(maxyIndex):
    for col in range(maxxIndex, -1, -1):
      for row in range(maxyIndex-1, -1, -1):
        if lst[row+1][col] == empty and lst[row][col] == block:
          lst[row][col] = empty
          lst[row+1][col] = block
  
  return lst

