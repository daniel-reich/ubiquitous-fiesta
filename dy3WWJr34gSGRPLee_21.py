
def make_box(n):
  return ['#'*n]+['#'+' '*(n-2)+'#']*(n-2)+['#'*n]*(n>1)

