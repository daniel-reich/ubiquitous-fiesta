
def minesweeper(grid):
  out= grid
  lst_qm = [(ix,jx) for ix, row in enumerate (grid) for jx,i in enumerate (row) if i=='?']
  lst_mine = [(ix,jx) for ix, row in enumerate (grid) for jx,i in enumerate (row) if i=='#']
  for tup in lst_qm:
    temp=[(tup[0]+i,tup[1]+j) for i in range (-1,2) for j in range (-1,2) if (tup[0]+i,tup[1]+j) in lst_mine]
    out[tup[0]][tup[1]]=str(len(temp))
  return out

