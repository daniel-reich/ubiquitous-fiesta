
def staircase(n):
  return staircase_r(1, n)[1:] if n > 0 else staircase_r(n, abs(n))[1:]
def staircase_r(n, l):
  if n == 0 or n == l+1:
    return ''
  return '\n' + '_'*(l-abs(n)) + '#'*(abs(n)) + staircase_r(n+1, l)

