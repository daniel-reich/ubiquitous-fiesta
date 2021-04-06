
def makeBox(n):
  if n == 1:
    return ['#']
  else:
    top = ['#'*n]
    bottom = ['#'*n]
    middle = ['#' + ' '*(n-2) + '#'] * (n-2)
    return top+middle+bottom

