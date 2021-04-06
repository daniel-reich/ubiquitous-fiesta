
def staircase(n, u=0):
    if abs(n) == u: return ''
    step = '_'*u + '#'*(abs(n)-u)
    return (step + '\n' + staircase(n, u+1)).rstrip('\n') if n< 0 \
      else (staircase(n, u+1) + '\n' + step).lstrip('\n')

