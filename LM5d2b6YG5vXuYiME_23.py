
def can_enter_cave(x):
  start = [[0,y] for y in range(len(x)) if x[y][0] == 0]
  moves = [(0,1), (1,0), (0,-1), (-1,0)]
  while True:
    count = len(start)
    for i in start:
      for j in moves:
        if 0 <= i[0]+j[0] < len(x[0]) and 0 <= i[1]+j[1] < len(x):
          if x[i[1]+j[1]][i[0]+j[0]] == 0 and [i[0]+j[0], i[1]+j[1]] not in start:
            if i[0]+j[0] == len(x[0])-1: return True
            start.append([i[0]+j[0], i[1]+j[1]])
    if len(start) == count:
      break
  return False

