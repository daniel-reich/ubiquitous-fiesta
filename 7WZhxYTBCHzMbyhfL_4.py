
def knight_bfs(a, b, c, d):
  movs = [[1,2], [1,-2], [2,1], [2,-1], [-1,2], [-1,-2], [-2,1], [-2, -1]]
  known = []
  toche = []
  known.append([a, b])
  toche.append([a, b])
  print (a, " ", b)
  while len(toche) > 0 :
    print(toche)
    che = toche[0]
    for move in movs:
      print(move)
      nx = che[0] + move[0]
      print(nx)
      ny = che[1] + move[1]
      print(nx, " " ,ny)
      if (1 <= nx <= 8) and (1 <= ny <= 8):
        if [nx, ny] not in known :
          known.append([nx, ny])
          toche.append([nx, ny])
    del toche[0]
    print(known)
    print(toche)
    exit()

