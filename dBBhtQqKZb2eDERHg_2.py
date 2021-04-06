
from math import ceil
def numberSequence(n):
    if n > 0:
        if n == 1:
            return '1'
        elif n == 2:
            return '1 1'
        else:
            return str(ceil(n/2)) + ' ' + numberSequence(n-2) + ' ' + str(ceil(n/2))
    else:
        return '-1'

