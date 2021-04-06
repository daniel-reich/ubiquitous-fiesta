
def is_vertical(l):
  return all(map(lambda x: x==l[0],l))
def is_horizontal(l):
  lt=[list(x) for x in zip(*l)]
  return is_vertical(lt)
def is_diagonal_left(l):
  d=[]
  for i in range(len(l)):
    d.append([l[x+i][x] for x in range(0,min(len(l)-i,len(l[0])))])
  for i in range(1,len(l[0])):
    d.append([l[x][x+i] for x in range(0,min(len(l),len(l[0]))-i)])
  ds=map(lambda x: set(x),d)
  return all(map(lambda x: len(x)==1,ds))
def is_diagonal_right(l):
  d=[]
  for i in range(len(l)):
    d.append([l[x+i][len(l[0])-1-x] for x in range(0,min(len(l)-i,len(l[0])))])
  for i in range(1,len(l[0])):
    d.append([l[x][len(l[0])-1-x-i] for x in range(0,min(len(l),len(l[0]))-i)])
  ds=map(lambda x: set(x),d)
  return all(map(lambda x: len(x)==1,ds))
def is_wristband(l):
  return is_vertical(l) or is_horizontal(l) or is_diagonal_left(l) or is_diagonal_right(l)

