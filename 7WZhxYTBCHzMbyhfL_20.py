
def knight_bfs(a, b, c, d):
  start,end=(a,b),(c,d)
  if start == end:
    return(0)
  piece_moves=[(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2),(2,1),(2,-1)]
  new_pos =(start[0],start[1])
  distance =((start[0]-end[0])**2 + (start[1]-end[1])**2)**.5
  i, min_distance=0,10
  while not (min_distance ==0 or i > 100):
    min_distance = 10
    for piece in piece_moves:
      if (new_pos[0]+piece[0]>0 and new_pos[1]+piece[1]>0 and new_pos[0]+piece[0]<9 and new_pos[1]+piece[1]<9):
        distance =((new_pos[0]+piece[0]-end[0])**2 + (new_pos[1]+piece[1]-end[1])**2)**.5
        horizontal_distance,vertical_distance= abs(new_pos[0]+piece[0]-end[0]),abs(new_pos[1]+piece[1]-end[1])
        if horizontal_distance+vertical_distance>2 or horizontal_distance+vertical_distance==0 or (horizontal_distance==0 and vertical_distance==2) or (horizontal_distance==2 and vertical_distance==0):
          if distance < min_distance:
            if (horizontal_distance == vertical_distance and distance >0):
              if(distance > 8**0.5):
                curr_pos=(new_pos[0]+piece[0],new_pos[1]+piece[1])
                min_distance=distance
            else:
              curr_pos=(new_pos[0]+piece[0],new_pos[1]+piece[1])
              min_distance=distance
    new_pos = curr_pos
    i+=1
  return i

