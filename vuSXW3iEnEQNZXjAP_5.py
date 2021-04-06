
def create_square(s):
  if not s or s<1: return ''
  if s==1: return '#'
  return '\n'.join(['#'*s] + ['#'+' '*(s-2)+'#']*(s-2) + ['#'*s])

