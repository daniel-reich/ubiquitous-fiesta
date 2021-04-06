
def bingo_check(b):
  if any(len(set(i))==1 for i in b): return True
  a =[[b[j][i] for j in range(len(b[i]))]for i in range(len(b))]
  c = len(set(b[i][i] for i in range(len(b))))==1
  d = len(set(b[i][-i-1] for i in range(len(b))))==1
  return any(len(set(i))==1 for i in a) or c or d

