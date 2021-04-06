
def magic_square_game(alice, bob):
  a, b = [], []
  
  for i in range(1,4):
    if i == alice[0]:
      a.append([int(alice[1][0]),int(alice[1][1]),int(alice[1][2])])
    else :
      a.append([0,0,0])
  
  if bob[0] == 1:
    b.append([int(bob[1][0]),0,0])
    b.append([int(bob[1][1]),0,0])
    b.append([int(bob[1][2]),0,0])
  elif bob[0] == 2:
    b.append([0,int(bob[1][0]),0])
    b.append([0,int(bob[1][1]),0])
    b.append([0,int(bob[1][2]),0])
  else :
    b.append([0,0,int(bob[1][0])])
    b.append([0,0,int(bob[1][1])])
    b.append([0,0,int(bob[1][2])])
  
  return a[alice[0]-1][bob[0]-1] == b[alice[0]-1][bob[0]-1]

