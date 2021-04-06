
def staircase(N, n=None, stairs=None):
    if not (n or stairs):
        n = 1
        stairs = []
    if n > abs(N):
        if N < 0:
            stairs = stairs[::-1]
        return '\n'.join(stairs)
        
    stairs.append('_'*(abs(N)-n) + '#'*n)
    return staircase(N, n+1, stairs)

