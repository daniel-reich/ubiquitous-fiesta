
def create_square(n):
    if n is None or n < 1:
        return ''
    if n == 1:
        return '#'
    return '\n'.join(['#'*n] + ['#{}#'.format(' '*(n-2))] * (n-2) + ['#'*n])

