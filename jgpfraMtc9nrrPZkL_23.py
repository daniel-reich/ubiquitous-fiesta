
def fall(x,y,lst):
  lst[y][x] = "-"
  while (y+1 < len(lst) and lst[y+1][x] != "#"):
    y += 1
  lst[y][x] = "#"
​
def switch_gravity_on(lst):
  for y in range(len(lst)-1, -1, -1):
    for x in range(len(lst[0])):
      if (lst[y][x] == "#"):
        fall(x,y,lst)
  return lst

