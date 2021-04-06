
moves=[[1,2], [1,-2], [2,1], [2,-1], [-1,2], [-1,-2], [-2,1], [-2, -1]]
​
​
def knight_bfs(a, b, c, d):
  print(a,b,c,d)
  data= [ [a,b] ]
​
  print(data)
  for counter in range(0,20):
    if [c,d] in data:
      return(counter)
    datanew=[]
    for x,y in [[x+m[0],y+m[1]] for m in moves for x,y in data ]:
      if x>0 and x<9 and y>0 and y<9:
        if not [x,y]  in datanew:
          datanew.append([x,y])
    data=datanew
    print(data)

