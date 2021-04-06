
def switch_gravity_on(lst):
​
  lst = move_down(lst)
​
  for i in range(len(lst) - 1):
    if "#" in lst[i]:
      lst = move_down(lst)
      
  return lst
​
def move_down(lst):
  for i in range(len(lst) - 1):
    for j in range(len(lst[0])):
      if lst[i][j] == "#" and lst[i + 1][j] != '#':
        lst[i][j] = '-'
        lst[i+1][j] = '#'
  return lst

