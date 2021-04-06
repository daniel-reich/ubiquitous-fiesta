
def mountain(lst,x):
  state = 'up'
  while x+1<len(lst):
    if state == 'up':
      if lst[x] > lst[x+1]:
        state = 'down'
    elif state == 'down':
      if lst[x] < lst[x+1]:
        return 'neither'
    x += 1
  if state == 'down':
    return 'mountain'
  return 'neither'
​
def valley(lst,x):
  state = 'down'
  while x+1<len(lst):
    if state == 'down':
      if lst[x] < lst[x+1]:
        state = 'up'
    elif state == 'up':
      if lst[x] > lst[x+1]:
        return 'neither'
    x += 1
  if state == 'up':
    return 'valley'
  return 'neither'
​
def landscape_type(lst):
  x = 1
  landscape = "neither"
  while x<len(lst):
    if lst[x] > lst[x-1]:
      landscape = mountain(lst,x)
      break
    elif lst[x] < lst[x-1]:
      landscape = valley(lst,x)
      break
    x+=1
  return landscape

