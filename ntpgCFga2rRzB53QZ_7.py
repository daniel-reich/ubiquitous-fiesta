
def staircase(n, u=0):
    if abs(n) == u:
        return ''
    new = '_' * u + '#' * (abs(n) - u)
    if n > 0:
        return (staircase(n, u+1) + '\n' + new).strip()
    else:
        return (new + '\n' + staircase(n, u+1)).strip()

