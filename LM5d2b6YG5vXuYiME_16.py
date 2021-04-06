
def can_enter_cave(cave):
  height, width = len(cave), len(cave[0])
  start = [[0, i] for i in range(len(cave)) if cave[i][0] == 0]
​
  def neighbors(c):
    x, y = c
    n = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
    n = [[x, y] for x,y in n if x in range(width) and y in range(height) and cave[y][x] == 0]
    return n
      
  for first in start:
    current=[first]
    next = []
    seen = []
    while current:
      for c in current:
        for n in neighbors(c):
          if n not in seen and n not in next:
            next.append(n)
            if n[0] == width-1:
              return True
        seen.append(c)
      current, next = next, []
  return False

