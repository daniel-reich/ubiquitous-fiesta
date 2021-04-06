
def is_legitimate(mtrx):
  inv_mtrx = [list(row) for row in zip(*mtrx)]
  return 1 not in mtrx[0]+mtrx[len(mtrx)-1]+inv_mtrx[0]+inv_mtrx[len(inv_mtrx)-1]

