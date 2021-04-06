
def largest_island(lst):
  mx=0
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      marked=[]
      if lst[i][x]==1:
        marked.append([i,x])
        marked = findisland(marked,lst)
        if len(marked)>mx:
          mx = len(marked)
  return mx
​
def findisland(marked,lst):
  init = marked
  for i in init:
    marked = leftright(lst,i,marked)
    marked = updown(lst,i,marked)
    marked = diag(lst,i,marked)
  if len(init)<len(marked):
    marked = findisland(marked,lst)
  else:
    return marked
​
def leftright(lst, place, marked):
  if place[1] > 0:
    if lst[place[0]][place[1]-1] == 1 and [place[0],place[1]-1] not in marked:
      marked.append([place[0],place[1]-1])
  if place[1] < len(lst[0])-1:
    if lst[place[0]][place[1]+1] and [place[0],place[1]+1] not in marked:
      marked.append([place[0],place[1]+1])
  return marked
  
def updown(lst, place, marked):
  if place[0] > 0:
    if lst[place[0]-1][place[1]] == 1 and [place[0]-1,place[1]] not in marked:
      marked.append([place[0]-1,place[1]])
  if place[0] < len(lst)-1:
    if lst[place[0]+1][place[1]] and [place[0]+1,place[1]] not in marked:
      marked.append([place[0]+1,place[1]])
  return marked
  
def diag(lst, place, marked):
  if place[0] > 0 and place[1] > 0:
    if lst[place[0]-1][place[1]-1] == 1 and [place[0]-1,place[1]-1] not in marked:
      marked.append([place[0]-1,place[1]-1])
  if place[0] < len(lst)-1 and place[1] < len(lst[0])-1:
    if lst[place[0]+1][place[1]+1] and [place[0]+1,place[1]+1] not in marked:
      marked.append([place[0]+1,place[1]+1])
  if place[0] > 0 and place[1] < len(lst[0])-1:
    if lst[place[0]-1][place[1]+1] == 1 and [place[0]-1,place[1]+1] not in marked:
      marked.append([place[0]-1,place[1]+1])
  if place[0] < len(lst)-1 and place[1] > 0:
    if lst[place[0]+1][place[1]-1] and [place[0]+1,place[1]-1] not in marked:
      marked.append([place[0]+1,place[1]-1])
  return marked

