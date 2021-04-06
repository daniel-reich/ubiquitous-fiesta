
def staircase(n):
  if n == 1 or n == -1: return '#'
  if n > 0:
    pre_str = staircase(n - 1).split('\n')
    new_str = ['_' + s for s in pre_str] + ['#' * n]
  if n < 0:
    pre_str = staircase(n + 1).split('\n')
    new_str = ['#' * -n] + ['_' + s for s in pre_str]
  return '\n'.join(new_str)

