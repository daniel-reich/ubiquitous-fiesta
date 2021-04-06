
def makeBox(n):
  if n == 1: return ['#']
  return ['#' * n] + ['#' + ' ' * (n - 2) + '#'] * (n - 2) + ['#' * n]

