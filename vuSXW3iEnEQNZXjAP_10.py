
def create_square(n):
    '''
    Returns a string which can be printed out as a square of dimension n as per
    the instructions
    '''
    if n is None: return ''
    return '\n'.join('#'*n if i==1 or i==n else '#'+' '*(n-2)+'#'
                     for i in range(1,n+1))

