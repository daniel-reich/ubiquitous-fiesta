
def move(mat, s=' '):
  if s[0] == 'u': return lambda p: move(mat[1:] + [mat[0]], p)
  if s[0] == 'd': return lambda p: move([mat[-1]] + mat[:-1], p)
  if s[0] == 'l': return lambda p: move([r[1:] + [r[0]] for r in mat], p)
  if s[0] == 'r': return lambda p: move([[r[-1]] + r[:-1] for r in mat], p)
  return mat if s[0] == 's' else lambda p: move(mat, p)

