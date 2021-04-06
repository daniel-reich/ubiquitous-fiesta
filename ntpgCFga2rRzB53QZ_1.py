
def staircase(n):
  if n<0: return '\n'.join(staircase(-n).split('\n')[::-1])
  if n==1: return '#'
  return '\n'.join(['_' + l for l in staircase(n-1).split('\n')]+['#'*n])

