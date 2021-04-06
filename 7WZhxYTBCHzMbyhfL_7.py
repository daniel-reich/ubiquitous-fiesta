
def knight_bfs(a, b, c, d):
  KNIGHT_MOVES = [(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]
  positions_at_move = [{(a,b)}]
  if (a,b)==(c,d):
    return 0
  while sum(len(positions) for positions in positions_at_move)<64:
    positions_at_move.append(set())
    for h,k in positions_at_move[-2]:
      for dx,dy in KNIGHT_MOVES:
        x,y = h+dx,k+dy
        if 0<x<=8 and 0<y<=8:
          if (x,y)==(c,d):
            return len(positions_at_move)-1
          elif not any((x,y) in positions for positions in positions_at_move):
            positions_at_move[-1].add((x,y))
  return -1

