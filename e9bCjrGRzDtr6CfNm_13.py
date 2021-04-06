
def solve(a, b):
    '''
    Solves ax=bx-3a+4 or flags no solution if values don't allow thia.
    '''
    try:
        if a == b == 2:
            return 'Any number'   # -> 2x-2 = 2x-2
        return round((b-3*a+4)/(a-b),3)
    except:
        return 'No solution'

