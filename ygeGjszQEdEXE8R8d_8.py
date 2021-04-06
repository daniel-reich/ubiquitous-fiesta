
def move(arg, mat=[[1]]):
  go = lambda a: lambda b: move(b, a)
  if arg == 'up': return go(mat[1:] + [mat[0]])
  if arg == 'down': return go([mat[-1]] + mat[:-1])
  if arg == 'left': return go([i[1:]+[i[0]] for i in mat])
  if arg == 'right': return go([[i[-1]]+i[:-1] for i in mat])
  if arg == 'stop': return mat
  return go(arg)

