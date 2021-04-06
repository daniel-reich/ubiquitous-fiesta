
def harry(po, r=0, c=0):
  if po == [[]]: return -1
  if r>=len(po) or c>=len(po[0]): return 0
  return po[r][c] + max(harry(po, r+1, c), harry(po, r, c+1))

