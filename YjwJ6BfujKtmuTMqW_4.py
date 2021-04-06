
def dice_game(scores):
  players,j=4,0
  players_out=[]
  p=[1,2,3,4]
  while (j < len(scores)):
    minn=(100,100)
    again=False
    k=0
    for i in range (j,j+players):
      if sum(scores[i]) <= sum((minn)):
        if sum(scores[i]) == sum((minn)):
          if scores[i][0]==minn[0]:
            again=True
          else:
            if scores[i][0]<minn[0]:
              minn = scores[i]
              index=p[k]
              again=False
        else:
          minn = scores[i]
          index=p[k]
          again=False
      k+=1
    j=j+players
    if not (again):
      players-=1
      p.remove(index)
      players_out.append('p'+ str(index))
  return ['p'+str(i) for i in range(1,5) if 'p'+str(i) not in players_out][0]

