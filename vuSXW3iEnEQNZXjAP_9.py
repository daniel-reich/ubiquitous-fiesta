
def create_square(n):
  return '\n'.join(['#'*n] + ['#'+' '*(n-2)+'#' for _ in range(n-2)]+['#'*n]*(n>1)) if n else ""

