
def can_enter_cave(x):
  global pos,d
  pos=[0,0]
  d=[0,1,0,1]
  c=len(x)*len(x[0])
  while pos[0]!=len(x[0])-1:
    c-=1
    if c==0:
      return False
    if d[3]==1:
      if x[pos[1]][pos[0]+1]==0:
        right()
        continue
    if d[0]==1:
      if x[pos[1]-1][pos[0]]==0:
        up()
        continue
    if d[1]==1:
      if x[pos[1]+1][pos[0]]==0:
        down()
        continue
    if d[2]==1:
      if x[pos[1]][pos[0]-1]==0:
        left()
        continue
    [down(),up(),right(),left()][p]
    d[p]=0
  return True
def up():
  global pos,d,p
  pos[1]-=1
  d=[1,0,1,1]
  p=0
  print("up")
def down():
  global pos,d,p
  pos[1]+=1
  d=[0,1,1,1]
  p=1
  print("down")
def left():
  global pos,d,p
  pos[0]-=1
  d=[1,1,1,0]
  p=2
  print("left")
def right():
  global pos,d,p
  pos[0]+=1
  d=[1,1,0,1]
  p=3
  print("right")

