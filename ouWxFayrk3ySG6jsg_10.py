
def who_won(b):
  for r in b:
    if len(set(r)) == 1:  return r[0]
    
  for c in zip(*b):
    if len(set(c)) == 1: return c[0]
  
  if b[0][0] == b[1][1] == b[2][2]: return b[0][0]
  
  if b[0][2] == b[1][1] == b[2][0]: return b[0][2]

