
def check(lst):
​
  for i in range(len(lst)-1):
    if lst[i+1] <= lst[i]:
      direction = 'down'
      break
    direction = 'increasing'
  
  if direction == 'down':
    for i in range(len(lst)-1):
      if lst[i+1] >= lst[i]:
        direction = 'neither'
        break
      direction = 'decreasing'
  
  return direction

