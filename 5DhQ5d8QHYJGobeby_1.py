
def hot_brick(t, n=10, m=0): #generalized for bricks of any size
  brick = build_brick(n)
​
  adj = ((1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1),(0,1),(0,-1))
  for _ in range(t):
    temp_brick = []
    for i in range(len(brick)-1):
      temp_row = []
      for j in range(len(brick[0])):
        s = brick[i][j]
        for x, y in adj:
          if i+x >= 0 and j+y >= 0:
            try:
              s += brick[i+x][j+y]
            except:
              s += 25
          else:
            s += 25
        temp_row.append(round(s/9))
      temp_brick.append(temp_row)
    temp_brick.append([90]*len(brick[0]))
    brick = temp_brick
  return brick
​
def build_brick(n, m=0):
  if not m:
    m = n
​
  brick = []
  for _ in range(n-1):
    brick.append([25]*m)
  brick.append([90]*m)
  return brick

