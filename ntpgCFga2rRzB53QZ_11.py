
def staircase(n, r=None, i=1):
  if r is None: r = list()
  if i == abs(n)+1: return '\n'.join([r, r[::-1]][n < 0])
  r += [''.join(['_'*(abs(n)-i), '#'*i])]
  return staircase(n, r, i+1)

