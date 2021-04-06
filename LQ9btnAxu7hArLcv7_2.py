
def diagonalize(n, d):
  a = [list(range(i, i + n)) for i in range(n)]
  if d == 'ul':
    return a
  if d == 'ur':
    return [v[::-1] for v in a]
  if d == 'll':
    return a[::-1]
  if d == 'lr':
    return [v[::-1] for v in a[::-1]]

