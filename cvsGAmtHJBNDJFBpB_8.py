
def can_traverse(x):
  moves,start,end=[(-1,1),(0,1),(1,1)],(len(x)-1,0),[(i,len(x[0])-1) for i in range (len(x))]
  current, column =start,0
  while column< len(x[0])-1:
    progress=False
    for move in moves:
      if current[0] + move[0] < len(x) and current[1] + move[1] < len(x[0]):
        if current[0] + move[0] == len(x)-1:
          if x[current[0] + move[0]][current[1] + move[1]] ==0:
            column=current[1] + move[1]
            temp= (current[0] + move[0],current[1] + move[1])
            current=temp
            progress=True
        else:
          if x[current[0] + move[0]][current[1] + move[1]] ==0 and x[current[0] + move[0]+1][current[1] + move[1]]==1:
            column=current[1] + move[1]
            temp= (current[0] + move[0],current[1] + move[1])
            current=temp
            progress=True
    if not (progress):
      break
  return not(bool(column%(len(x[0])-1))) if column>1 else False

